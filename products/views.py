from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product, Category
from django.db.models import Q

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    query = request.GET.get('q')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(amount__icontains=query)).distinct()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, "products/list.html", context)

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, "products/detail.html", context)

def byCategory(request, category_id, slug):
    categories = Category.objects.all()
    products = Product.objects.filter(category_id=category_id)
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, "products/by_category.html", context)

def search(request):
    return render(request, "products/search.html")
