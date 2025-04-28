from django.shortcuts import render
from .models import Category,Product
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

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

def ProductView(request,pk):
    product=get_object_or_404(Product,pk=pk)
    return render(request,'product_view.html',{'product':product})

def Shop(request):
    product=Product.objects.all()
    paginator = Paginator(product, 12)
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)
    return render(request,'shop.html',{'product':product,'page_obj': page_obj})

def Filter(request):
    product = Product.objects.all()
    category_list = Category.objects.all()
    price_min = request.GET.get('price_min', None)
    price_max = request.GET.get('price_max', None)
    if price_min and price_max:
        product = product.filter(Price__gte=price_min, Price__lte=price_max)
    category = request.GET.get('category', None)
    if category:
        product = product.filter(category_id=category)
    paginator = Paginator(product.order_by('Name'), 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop.html', {'page_obj': page_obj,'category': category_list})

def ShopCategory(request):
    product = Product.objects.all()
    category_list = Category.objects.all()
    category = request.GET.get('category', None)
    if category:
        product = product.filter(category_id=category)
    paginator = Paginator(product.order_by('Name'), 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop_by_category.html', {'page_obj': page_obj,'category': category_list})

