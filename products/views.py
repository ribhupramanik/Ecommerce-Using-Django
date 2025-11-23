from django.shortcuts import render, get_object_or_404
from .models import Product, ProductReview
from .forms import ReviewForm
from django.db.models import Q

# Create your views here.

def home(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(
            Q(name_icontains=query) | Q(description_icontains=query)
        )
    else:
        products = Product .objects.all()
    return render (request, "products/home.html",{
        'products': products,
        'query': query
    })

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()

    form = ReviewForm()

    if request.method == "POST":

        review = ProductReview.objects.create(
            user=request.user,
            product=product,
            rating=request.POST['rating'],
            review_text=request.POST.get('review_text')
        )

        product.update_rating()
    
    return render(request, "products/product_detail.html",{
        "product": product,
        "reviews": reviews,
        "form": form
    })