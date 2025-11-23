from django.urls import path
from .views import home, product_details

urlpatterns = [
    path('', home, name="home"),
    path('product/<int:product_id>/', product_details, name="product_detail"),
]
