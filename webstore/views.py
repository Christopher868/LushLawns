from django.shortcuts import render, redirect
from .models import Brand, Mower_Model, Part


# View for homepage that displays all brands
def home(request):
    brand = Brand.objects.all()
    return render(request, 'webstore/home.html', {'brand': brand})


# View for all models page that displays all available models
def all_models(request):
    models = Mower_Model.objects.all()
    return render(request, 'webstore/all-models.html', {'models': models})


# View for all parts page that display all available models 
def all_parts(request):
    parts = Part.objects.all()
    return render(request, 'webstore/all-parts.html', {'parts':parts})


# View for cart page
def cart(request):
    return render(request, 'webstore/cart.html', {})


# View for models page that displays models based upon brand clicked by user
def models(request, brand_name):
    brand_name = brand_name.replace('-', ' ')
    brands = Brand.objects.get(name=brand_name)
    models = Mower_Model.objects.filter(brand=brands)
    return render(request, 'webstore/models.html', {'models':models, 'brands':brands})


# View for parts page that displays parts based on model clicked on by users
def parts(request, model_num):
    model_num = model_num.replace('-', ' ')
    model = Mower_Model.objects.get(model_number=model_num)
    parts = Part.objects.filter(mower_model=model)
    return render(request, 'webstore/parts.html', {'parts':parts, 'model':model})
