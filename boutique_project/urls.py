"""
URL configuration for boutique_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from products_app import views as product_view
from user_accounts_app import views as user_view
from cart_app import views as cart_view
from wishlist_app import views as wishlist_view
from orders_app import views as order_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',product_view.LogHome,name='LogHome'),
    path('home',product_view.Home,name='home'),
    path('productview/<int:id>/', product_view.productview, name='productview'),
    path('productviewlogin/<int:id>/', product_view.productviewlogin, name='productviewlogin'),
    path('search',product_view.Search,name='search'),
    path('searchlog',product_view.SearchLog,name='searchlog'),
    path('about',product_view.About,name='about'),
    path('aboutlog',product_view.AboutLog,name='aboutlog'),
    path('privacy',product_view.PrivacyPolicy,name='privacy'),
    path('privacylog',product_view.PrivacyPolicyLog,name='privacylog'),
    path('terms',product_view.Terms,name='terms'),
    path('termslog',product_view.TermsLog,name='termslog'),
    path('login',user_view.LogPage,name='login'),
    path('logout',user_view.LogoutPage,name='logout'),
    path('profileedit',user_view.ProfileEdit,name='profileedit'),
    path('profile',user_view.Profile,name='profile'),
    path('passwordreset',user_view.password_reset_request,name='passwordreset'),
    path('verifyotp',user_view.verify_otp,name='verifyotp'),
    path('setnewpassword',user_view.set_new_password,name='setnewpassword'),
    path('signup',user_view.SignUp,name='signup'),
    path('changepassword',user_view.ChangePassword,name='changepassword'),
    path('addtocart/<int:product_id>', cart_view.AddToCart, name='addtocart'),
    path('cart/', cart_view.CartView, name='cart_view'),
    path('remove-from-cart/<int:cart_item_id>/', cart_view.RemoveCart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', cart_view.update_cart_quantity, name='update_cart_quantity'),
    path('shop',product_view.Shop,name='shop'),
    path('shoplog',product_view.ShopLog,name='shoplog'),
    path('filter',product_view.Filter,name='filter'),
    path('categoryhome',product_view.CategoryHome,name='categoryhome'),
    path('categoryhomelog',product_view.CategoryHomeLog,name='categoryhomelog'),
    path('shopbycategory/<int:pk>',product_view.ShopCategory,name='shopbycategory'),
    path('shopbycategorylog/<int:pk>',product_view.ShopCategoryLog,name='shopbycategorylog'),
    path('about',product_view.About,name='about'),
    path('sizechart',product_view.SizeChart,name='sizechart'),
    path('wishlist/<int:pk>/', wishlist_view.Wishlist, name='wishlist'),
    path('my-wishlist/', wishlist_view.Wishlist_View, name='wishlist_view'),
    path('toggle-wishlist/<int:product_id>/', wishlist_view.toggle_wishlist, name='toggle_wishlist'),
    path('placeorder', order_view.PlaceOrder, name='placeorder'),
    path('address', order_view.AddressChange, name='address'),
    path('verify-payment/', order_view.verify_payment, name='verify_payment'),
    path('order-success/<int:order_id>/', order_view.OrderSuccess, name='order_success'),
    path('orderdetails/<int:order_id>', order_view.order_detail, name='orderdetail'),
    path('my-orders/', order_view.my_orders, name='my_orders'),

    
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)