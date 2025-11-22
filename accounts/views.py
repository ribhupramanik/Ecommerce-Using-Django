from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, SellerRegistrationForm
from .models import CustomUser

# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
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
            user.role = 'SELLER'
            user.save()
            return redirect('login')
    else:
        form = SellerRegistrationForm()

    return render(request, 'accounts/seller_register.html', {'form': form})