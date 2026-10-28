from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
from django.contrib.auth.models import User


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
        username=request.POST['username']
        password=request.POST['password']
        #create user
        user=User.objects.create_user(username=username,password=password)
        user.save()
        messages.success(request,"You have been registered")
        return redirect('home')
    else:
        return render(request,'register.html')


def logout_view(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return render(request,'logout.html')

