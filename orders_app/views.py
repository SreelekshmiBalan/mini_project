from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart_app.models import Cart
from django.utils import timezone
import razorpay
from django.conf import settings

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
        'amount': total * 100,  # Razorpay needs amount in paise
        'currency': 'INR',
        'payment_capture': 1
    })

    context = {
        'cart_items': cart_items,
        'total': total,
        'razorpay_order_id': payment['id'],
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'user': request.user,
    }
    return render(request, 'place_order.html', context)


def OrderSuccess(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/order_success.html', {'order': order})
