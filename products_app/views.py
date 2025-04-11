from django.shortcuts import render
from .models import Category,Product
from django.http import HttpResponse


# Create your views here.
def LogHome(request):
    products=Product.objects.filter(New_Launch=True)
    categories=Category.objects.filter(Top_Category=True)
    best_sellers=Product.objects.filter(Best_Seller=True)
    return render(request,'login_home.html',{'products':products,'categories':categories,'best_sellers':best_sellers})

def Home(request):
    products=Product.objects.filter(New_Launch=True)
    categories=Category.objects.filter(Top_Category=True)
    best_sellers=Product.objects.filter(Best_Seller=True)
    return render(request,'home.html',{'products':products,'categories':categories,'best_sellers':best_sellers})
