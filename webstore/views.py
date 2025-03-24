from django.shortcuts import render, redirect
from .models import Brand, Mower_Model, Part
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm


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


# View for customer login page
def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method =="POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, ("Successful Login!"))
                return redirect('home')
            else:
                messages.success(request, ("Incorrect Username or Password!"))
                return redirect('login')
        else:
            return render(request, 'webstore/login.html', {})
        

# View for logging out user
def logout_user(request):
    logout(request)
    messages.success(request, ("Successfully Logged Out!"))
    return redirect('home')

# View for customer register page
def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, ("Account Successfully Created and Logged into!"))
                return redirect('home')
                
            else:
                messages.success(request, ("Error! 1 or more fields filled out incorrectly"))
                return render(request, 'webstore/register.html', {'form': form})

        else:
            form = CreateUserForm()
            return render(request, 'webstore/register.html', {'form': form})
