from django.shortcuts import render,redirect
from products_app.models import Product
from django.shortcuts import get_object_or_404
from .models import WishLists
from user_accounts_app.models import Account
from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.

def Wishlist(request,pk):
    if not request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'message': 'Login required'}, status=401)
        return redirect('login')
    product=get_object_or_404(Product,pk=pk)
    wishlist_item = WishLists.objects.filter(user=request.user, product=product).first()
    if wishlist_item:
        wishlist_item.delete()
        in_wishlist=False
    else:
        WishLists.objects.create(user=request.user, product=product)
        in_wishlist=True
    return redirect('wishlist_view')

def Wishlist_View(request):
    if not request.user.is_authenticated:
        return redirect('login')
    wishes = WishLists.objects.filter(user=request.user).select_related('product')
    return render(request, 'wishlist.html', {'wishes': wishes})

def toggle_wishlist(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')

    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = WishLists.objects.get_or_create(user=request.user, product=product)

    if not created:
        wishlist_item.delete()

    return redirect(request.META.get('HTTP_REFERER', 'product_list'))

from django.http import JsonResponse

# def add_to_wishlist(request, product_id):
#     if request.method == 'POST':
#         product = get_object_or_404(Product, id=product_id)
#         wishlist, created = WishLists.objects.get_or_create(user=request.user)

#         if product in wishlist.products.all():
#             wishlist.products.remove(product)
#             return JsonResponse({'status': 'removed'})
#         else:
#             wishlist.products.add(product)
#             return JsonResponse({'status': 'added'})


# def product_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     user_wishlist = WishLists.objects.filter(user=request.user).values_list('product_id', flat=True)
#     return render(request, 'product_view.html', {'product': product, 'user_wishlist': user_wishlist})

