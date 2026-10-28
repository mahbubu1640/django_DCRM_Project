from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
from django.contrib.auth.models import User
from .forms import SignUpForm

def home(request):
    #check to see if logging in 
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        #authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged In")
            return redirect('home')
        else:
            messages.success(request,"There was an Error")
            return redirect('home')
    else:
        return render(request,'home.html')

def register(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login user
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            #create user
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have been registered and logged in")
            user.save()
        else:
            messages.success(request,"There was an error registering the user")
        return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return render(request,'logout.html')

