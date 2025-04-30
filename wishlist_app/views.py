from django.shortcuts import render,redirect
from products_app.models import Product
from django.shortcuts import get_object_or_404
from .models import WishList

# Create your views here.

# def Wishlist(request,pk):
#     if request.method=='POST':
#         if 'wishlistbutton' in request.POST:
#             product=get_object_or_404(Product,pk=pk)
#             product_name=product.Name
#             product_code=product.Product_Code
#             price=product.Price
#             wish=WishList.objects.create(Product_Name=product_name,Product_Code=product_code,Product_Price=price)
#             wish.save()
#             return redirect(request,'product_view.html',{'wish':wish})
