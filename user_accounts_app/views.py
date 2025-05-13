from django.shortcuts import render,redirect
from .models import Account
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
import random
from django.core.mail import send_mail
from django.contrib import messages



# Create your views here.
def SignUp(request):
    if request.method == 'POST':
        UserName = request.POST['Username']
        Email=request.POST['Email']
        PassWord = request.POST['Password']
        confirm_password = request.POST['ConfirmPSW']
        if not UserName or not Email or not PassWord or not confirm_password:
            return render(request, 'signup.html', {'error': 'All fields are required.'})
        if PassWord != confirm_password:
            return render(request, 'signup.html', {'error': 'Passwords do not match.'})
        if Account.objects.filter(username=UserName).exists():
            return render(request, 'signup.html', {'error': 'Username already taken.'})
        user = Account(username=UserName, email=Email)
        user.set_password(PassWord)
        user.save()
        messages.success(request, 'Account created successfully. Please log in')
        return redirect('login')
    else:
        return render(request, 'signup.html')


def LogPage(request):
    error=''
    if request.method=='POST':
        UserName=request.POST['username']
        PassWord=request.POST['password']
        user=authenticate(request,username=UserName,password=PassWord)
        admin_user=authenticate(request,username=UserName,password=PassWord)
        if admin_user is not None and admin_user.is_staff:
            login(request,admin_user)
            return redirect('admin:index')
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error='Credentials not provided'
    else:
        # error='Please fill in both fields correctly'
        return render(request,'login.html',{'error':error})
    
def send_otp(email):
    otp = random.randint(100000,999999)
    send_mail(
        'Your OTP Code',''
        f'Your OTP code is: {otp}',
        'sreelekshmibalan01@gmail.com',
        [email],
        fail_silently=False,
    )
    return otp

def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = Account.objects.get(email=email)
            otp = send_otp(email)

            context = {
                        "email": email,
                        "otp": otp,
            }
            return render(request,'verify_otp.html',context)
        
        except Account.DoesNotExist:
            messages.error(request,'Email address not found.')
    else:
        return render(request,'password_reset.html')
    return render(request,'password_reset.html') 

def verify_otp(request):
    if request.method == 'POST':
        email =request.POST.get('email')
        otpold = request.POST.get('otpold')
        otp = request.POST.get('otp')

        if otpold==otp :
            context = {
                'otp' : otp,
                'email': email
            }
            return render(request,'set_new_password.html',context)
        else:
            messages.error(request,"Invalid OTP")
    return render(request,'verify_otp.html') 

def set_new_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password==confirm_password:
            try:
                data = Account.objects.get(email=email)
                # user=CustomUser.objects.get(id=data.user_id.id)
                data.set_password(new_password)
                data.save()
                messages.success(request,'Password has been reset successfully')
                return redirect(LogPage)
            except Account.DoesNotExist:
                messages.error(request,'Password doesnot match')
        return render(request,'set_new_password.html',{'email':email})               
    return render(request,'set_new_password.html',{'email':email})
