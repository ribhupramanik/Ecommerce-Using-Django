from django.urls import path
from .views import dashboard_home, add_product

urlpatterns = [
    path('', dashboard_home, name='dashboard_home'),
    path('add-product/', add_product, name="add_product"),
]