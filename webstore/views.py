from django.shortcuts import render, redirect, get_object_or_404
from .models import Brand, Mower_Model, Part, UserSession
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, EditUser
from django.contrib.auth.models import User
from itertools import chain
import json
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash




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


# View for viewing details on specific part
def part_info(request, part_num):
    part = Part.objects.filter(part_number = part_num).first()
    mower_model = part.mower_model.all()
    return render(request, 'webstore/part-info.html', {'part': part, 'mower_model': mower_model})




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
                try:
                    # Getting session information
                    user_session = UserSession.objects.get(user=user)
                    session_data = user_session.session_data
                    session_data = json.loads(session_data)
                #Check for session data then putting it into new session
                    if session_data:
                        for key, value in session_data:
                            request.session[key] = value

                except UserSession.DoesNotExist:
                    pass
                return redirect('home')
            else:
                messages.success(request, ("Incorrect Username or Password!"))
                return redirect('login')
        else:
            return render(request, 'webstore/login.html', {})
        

# View for logging out user
def logout_user(request):
    if request.user.is_authenticated:
        # Getting current session data
        session_data = json.dumps(list(request.session.items()))

        #Saving user's session data in model so it can be accessed later
        user_session, created = UserSession.objects.get_or_create(user=request.user)
        user_session.session_data = session_data
        user_session.save()
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
                messages.success(request, ("Account Successfully Created!"))
                return redirect('home')
                
            else:
                return render(request, 'webstore/register.html', {'form': form})

        else:
            form = CreateUserForm()
            return render(request, 'webstore/register.html', {'form': form})
        

#View for searching using the search bar
def search(request):
    if request.method == "POST":
        search = request.POST['search']
        model = Mower_Model.objects.filter(model_number__contains=search) 
        part = Part.objects.filter(part_number__contains=search)
        result = list(chain(model, part))
        return render(request, 'webstore/search.html', {'result':result, 'search': search})
    else:
        return render(request, 'webstore/search.html', {})
        

#View for viewing all user orders
def orders(request):
    return render(request, 'webstore/orders.html', {})


#View for viewing specific order details
def order_info(request):
    return render(request, 'webstore/order-info.html', {})


#View that allows user to change profile information
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditUser(request.POST, instance=request.user)
            if form.is_valid(): 
                form.save() 
                return redirect('profile')
            else:
                return render(request, 'webstore/profile.html', {'form': form})
        else:
            form = EditUser(instance=request.user)
    else:
        return redirect('login')
    
    return render(request, 'webstore/profile.html', {'form': form})

#View for page that allows user to change password 
def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)
            if form.is_valid(): 
                user = form.save() 
                update_session_auth_hash(request, user)
                return redirect('profile')
            else:
                return render(request, 'webstore/change-password.html', {'form': form})
        else:
            form = PasswordChangeForm(user=request.user)
    else:
        return redirect('login')
    return render(request, 'webstore/change-password.html', {'form':form})