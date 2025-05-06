from django.shortcuts import render
from .models import Cart
from products_app.models import Product
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.

def AddToCart(request,product_id):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to add items to the cart.")
        return redirect('login')

    product = get_object_or_404(Product, id=product_id)
    size = request.POST.get('size')
    quantity = request.POST.get('quantity', 1)

    if not size:
        messages.error(request, "Please select a size before adding to cart.")
        return redirect('productview', pk=product.id)

    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product, size=size)

    if not created:
        cart_item.quantity += int(quantity)
    else:
        cart_item.quantity = int(quantity)

    cart_item.save()
    messages.success(request, "Product added to cart.")
    return redirect('productview', pk=product.id)


@login_required
def CartView(request):
    cart_items = Cart.objects.filter(user=request.user)
    
    total_price = sum(item.product.Price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart/cart_view.html', context)


