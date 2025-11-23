from django.urls import path
from .views import login_view, verify_otp, user_register, seller_register, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('register/', user_register, name='user_register'),
    path('seller-register/', seller_register, name='seller_register'),
    path('logout/', logout_view, name='logout'),
]
