from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .models import Product,Category


# Create your views here.

def home(request):
    all_products = Product.objects.all()    
    return render(request, 'index.html',context={'all_products':all_products})

def register (request):
    register_form = NewUserForm (request.POST)
    if request.method =="POST":
        form_data = NewUserForm (request.POST)
        if form_data.is_valid():
            user = form_data.save()
            # login(request,user)
            return redirect ('login')

    return render(request,template_name="register.html",context={'register_form':register_form})



def login_user(request):
    if request.method == "POST":
        login_form = AuthenticationForm (request,data=request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,"Logged In Successfully")
                return redirect('home')
            else:
                messages.error(request,"Invalid Username or Password")
    form = AuthenticationForm()
    return render(request,template_name="login.html",context={"login_form":form})


def logout_user(request):
    logout(request)
    messages.info(request,"You have Logged Out")
    return redirect ("home")