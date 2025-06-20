from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem
from cart_app.models import Cart
from user_accounts_app.models import Account
from django.utils import timezone
import razorpay
from django.conf import settings
from django.http import JsonResponse
from razorpay.errors import SignatureVerificationError


# Create your views here.

def PlaceOrder(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items.exists():
        return redirect('cart')

    total = sum(int(item.product.Price) * item.quantity for item in cart_items)

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    payment = client.order.create({
        'amount': total * 100,
        'currency': 'INR',
        'payment_capture': 1
    })


    if request.user.is_authenticated:
        profile = request.user
        address1=profile.address_line_1
        address2=profile.address_line_2
        district=profile.district
        state=profile.state
        pincode=profile.pin_code
        phone=profile.phone
    else:
        address1=""
        address2=""
        district=""
        state=""
        pincode=""
        phone=""

    context = {
        'cart_items': cart_items,
        'total': total,
        'razorpay_order_id': payment['id'],
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'user': request.user,
        'address1': address1,
        'address2':address2,
        'district':district,
        'state':state,
        'pincode':pincode,
        'phone':phone
    }

    return render(request, 'place_order.html', context)


def OrderSuccess(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/order_success.html', {'order': order})

def verify_payment(request):
    if request.method == "POST":
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_signature = request.POST.get('razorpay_signature')
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
            
        }

        try:
            client.utility.verify_payment_signature(params_dict)

            # Proceed with creating the order
            cart_items = Cart.objects.filter(user=request.user)
            total = sum(item.product.Price * item.quantity for item in cart_items)
            order = Order.objects.create(
                user=request.user,
                total_amount=total,
                status='Order placed',
                shipping_address=request.POST.get('address', "No address provided"),  # Add shipping address
                payment_method="Razorpay",
                is_paid=True,
                paid_at=timezone.now(),
                razorpay_order_id=razorpay_order_id,
                razorpay_payment_id=razorpay_payment_id,
                razorpay_signature=razorpay_signature
            )

            # Create the OrderItems
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    size=item.size,
                    quantity=item.quantity,
                    price=item.product.Price
                )

            # Empty the cart after successful payment
            cart_items.delete()

            # Return success JSON response with order_id
            return JsonResponse({
                'success': True,
                'order_id': order.id,
            })

        except SignatureVerificationError:
            # In case of a signature mismatch
            return JsonResponse({
                'success': False,
                'error': 'Payment verification failed',
            })

def order_detail(request, order_id):
    if not request.user.is_authenticated:
        return redirect('login')
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order_detail.html', {'order': order})

def my_orders(request):
    if not request.user.is_authenticated:
        return redirect('login')
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_orders.html', {'orders': orders})

def AddressChange(request):
    userdata=Account.objects.get(id=request.user.id)
    if request.method=='POST':
        userdata.address_line_1=request.POST.get('address_line1')
        userdata.address_line_2=request.POST.get('address_line2')
        userdata.district=request.POST.get('district')
        userdata.state=request.POST.get('state')
        userdata.pin_code=request.POST.get('postal_code')
        userdata.phone=request.POST.get('phone')
        userdata.save()
        return redirect('placeorder')
    else:
        return render(request,'address_change.html')

