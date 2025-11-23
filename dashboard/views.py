from django.shortcuts import render, redirect
from accounts.utils import role_required
from products.models import Product
from products.forms import ProductForm

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

    return render(request, "dashboard/dashboard_home.html", context)

@role_required(allowed_roles=["ADMIN", "SELLER"])
def add_product(request):
    form = ProductForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect("dashboard_home")
    return render(request, "dashboard/add_product.html", {"form": form})
