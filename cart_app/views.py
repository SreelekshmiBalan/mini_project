from django.shortcuts import render
from .models import Cart
from products_app.models import Product
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.

def AddToCart(request,product_id):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to add items to the cart.")
        return redirect('login')

    product=Product.objects.get(id=product_id)
    size=request.POST['size']
    quantity=request.POST.get('quantity', 1)
    cart_item,created= Cart.objects.get_or_create(user=request.user,product=product)
    if not created:
        cart_item.quantity += int(quantity)
    else:
        cart_item.quantity = int(quantity)
    cart_item.size=size
    cart_item.save()
    return redirect('productview')
