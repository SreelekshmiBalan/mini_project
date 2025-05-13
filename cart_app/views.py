from django.shortcuts import render
from .models import Cart
from products_app.models import Product
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.

def AddToCart(request, product_id):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to add items to the cart.")
        return redirect('login')

    product = get_object_or_404(Product, id=product_id)
    size = request.POST.get('size')
    quantity = request.POST.get('quantity', 1)

    if not size:
        messages.error(request, "Please select a size before adding to cart.")
        return redirect('productview', id=product.id)

    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product, size=size)

    if not created:
        cart_item.quantity += int(quantity)
    else:
        cart_item.quantity = int(quantity)

    cart_item.save()
    messages.success(request, "Product added to cart.")
    return redirect('productview', id=product.id)




def CartView(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.Price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)

def RemoveCart(request, cart_item_id):
    item = get_object_or_404(Cart, id=cart_item_id)
    item.delete()
    return redirect('cart_view')

def update_cart_quantity(request, item_id):
    item = get_object_or_404(Cart, id=item_id)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'increase':
            item.quantity += 1
        elif action == 'decrease' and item.quantity > 1:
            item.quantity -= 1
        item.save()
    
    return redirect('cart_view')

