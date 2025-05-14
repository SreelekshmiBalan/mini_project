from django.shortcuts import render
from .models import Category,Product
from wishlist_app.models import WishLists
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from cart_app.models import Cart
from wishlist_app.models import WishLists

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

from cart_app.models import Cart

def productview(request, id):
    product = get_object_or_404(Product, id=id)
    in_wishlist = WishLists.objects.filter(user=request.user, product=product).exists() if request.user.is_authenticated else False

    product_in_cart = False
    if request.user.is_authenticated:
        product_in_cart = Cart.objects.filter(user=request.user, product=product).exists()

    size_list = ['XS', 'S', 'M', 'L', 'XL', '2XL', '3XL']  # Or pull from DB if dynamic

    return render(request, 'product_view.html', {
        'product': product,
        'in_wishlist': in_wishlist,
        'product_in_cart': product_in_cart,
        'size_list': size_list,
    })




# def ProductView(request, pk):
#     product = get_object_or_404(Product, pk=pk)

#     in_wishlist = False
#     if request.user.is_authenticated:
#         in_wishlist = WishLists.objects.filter(user=request.user, product=product).exists()

#     context = {
#         'product': product,
#         'in_wishlist': in_wishlist,
#     }
#     return render(request, 'product_view.html', context)

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

def CategoryHome(request):
    category=Category.objects.all()
    return render(request,'category_home.html',{'categories':category})

def ShopCategory(request,pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    return render(request,'shop_by_category.html',{'category':category, 'products':products})
    # product = Product.objects.all()
    # category_list = Category.objects.all()
    # category = request.GET.get('category', None)
    # if category:
    #     product = product.filter(category_id=category)
    # paginator = Paginator(product.order_by('Name'), 12)
    # page_number = request.GET.get('page', 1)
    # page_obj = paginator.get_page(page_number)
    # return render(request, 'shop_by_category.html', {'page_obj': page_obj,'category': category_list})

def About(request):
    return render(request,'about.html')

def SizeChart(request):
    return render(request,'size_chart.html')




