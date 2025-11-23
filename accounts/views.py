from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, SellerRegistrationForm
from .models import CustomUser
import random
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q

# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.role = "USER"
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request,'accounts/user_register.html', {'form':form})

def seller_register(request):
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.role = 'SELLER'
            user.save()
            return redirect('login')
    else:
        form = SellerRegistrationForm()

    return render(request, 'accounts/seller_register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        login_value = request.POST.get('login_value')  
        password = request.POST.get('password')

        try:
            # Search user by username OR email
            user = CustomUser.objects.get(
                Q(username=login_value) | Q(email=login_value)
            )
        except CustomUser.DoesNotExist:
            return render(request, 'accounts/login.html', {
                'error': "User not found"
            })

        if user.check_password(password):

            if user.role == "ADMIN":
                login(request, user)
                return redirect('home')
            
            otp = str(random.randint(100000, 999999))
            user.otp = otp
            user.save()

            send_mail(
                subject="Your OTP",
                message=f"Your OTP is {otp}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],   # Always send to registered email
            )

            request.session['user_id'] = user.id
            return redirect('verify_otp')

        
        else:
            return render(request, 'accounts/login.html',{
                'error': "Invalid credentials"
            })
    
    return render(request, 'accounts/login.html')

def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        user_id = request.session.get('user_id')

        user = CustomUser.objects.get(id=user_id)

        if user.otp == otp:
            user.otp = ''
            user.save()
            login(request, user)
            return redirect('home')
    
    return render(request, 'accounts/verify_otp.html')