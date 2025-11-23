from django.shortcuts import render
from accounts.utils import role_required
from products.models import Product

# Create your views here.

@role_required(allowed_roles=["ADMIN", "SELLER"])
def dashboard_home(request):
    if request.user.role == "SELLER":
        products = Product.objects.filter(seller=request.user)
    else:
        products = Product.objects.all()
    
    total_products = products.count()

    total_stock = sum(p.stock for p in products)

    context = {
        "products": products,
        "total_products": total_products,
        "total_stock": total_stock
    }

    return render(request, "dashboard_home.html", context)
