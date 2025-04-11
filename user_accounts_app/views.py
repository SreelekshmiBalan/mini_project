from django.shortcuts import render,redirect
from .models import Account
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout



# Create your views here.
def LogPage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,Username=username,Password=password)
        admin_user=authenticate(request,Username=username,Password=password)
        if admin_user is not None and admin_user.is_staff:
            login(request,admin_user)
            return redirect('admin:index')
        if user is not None:
            login(request,user)
        else:
            return render(request,'home.html',{'error':'Credentials not provided'})
    else:
        return render(request,'login.html')
