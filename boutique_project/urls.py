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

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('',product_view.LogHome,name='LogHome'),
    path('home',product_view.Home,name='home'),
    path('productview/<int:pk>',product_view.ProductView,name='productview'),
    path('login',user_view.LogPage,name='login'),
    path('passwordreset',user_view.password_reset_request,name='passwordreset'),
    path('verifyotp',user_view.verify_otp,name='verifyotp'),
    path('setnewpassword',user_view.set_new_password,name='setnewpassword'),
    path('signup',user_view.SignUp,name='signup'),
    path('addtocart/<int:id>',cart_view.AddToCart,name='addtocart'),
    path('shop',product_view.Shop,name='shop'),
    path('filter',product_view.Filter,name='filter'),
    path('shopbycategory/<int:pk>',product_view.ShopCategory,name='shopbycategory'),
    path('about',product_view.About,name='about'),
    path('wishlist/<int:pk>',wishlist_view.Wishlist,name='wishlist'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)