from django.shortcuts import render, redirect
from .models import Brand, Mower_Model

def home(request):
    brand = Brand.objects.all()
    return render(request, 'webstore/home.html', {'brand': brand})

def all_models(request):
    return render(request, 'webstore/all-models.html', {})

def all_parts(request):
    return render(request, 'webstore/all-parts.html', {})

def cart(request):
    return render(request, 'webstore/cart.html', {})

def models(request, brand_name):
    brand_name = brand_name.replace('-', ' ')
    brands = Brand.objects.get(name=brand_name)
    models = Mower_Model.objects.filter(brand=brands)
    return render(request, 'webstore/models.html', {'models':models, 'brands':brands})
