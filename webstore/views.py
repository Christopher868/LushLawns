from django.shortcuts import render, redirect

def home(request):
    return render(request, 'webstore/home.html', {})

def all_models(request):
    return render(request, 'webstore/all-models.html', {})

def all_parts(request):
    return render(request, 'webstore/all-parts.html', {})
