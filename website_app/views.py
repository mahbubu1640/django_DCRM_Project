from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Record

def home(request):
    #get all records from the database
    records = Record.objects.all()

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
        return render(request,'home.html', {'records': records})

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



def record_detail(request, pk):
    if request.user.is_authenticated:
        #look up record
        records = Record.objects.get(id=pk)
        return render(request,'record.html', {'records': records})
    else:
        messages.success(request,"You must be logged in to view that page")
        return redirect('home')

def record_update(request, pk):
    if request.user.is_authenticated:
        #look up record
        records = Record.objects.get(id=pk)
        if request.method == "POST":
            records.first_name = request.POST['first_name']
            records.last_name = request.POST['last_name']
            records.email = request.POST['email']
            records.phone = request.POST['phone']
            records.address = request.POST['address']
            records.city = request.POST['city']
            records.zipcode = request.POST['zipcode']
            records.save()
            messages.success(request,"Record updated successfully")
            return redirect('record_detail', pk=records.id)
        else:
            return render(request,'record_update.html', {'records': records})
    else:
        messages.success(request,"You must be logged in to update a record")
        return redirect('home')

def record_delete(request,pk):
    if request.user.is_authenticated:
        #look up record
        records=Record.objects.get(id=pk)
        records.delete()
        messages.success(request,"Record deleted successfully")
        return redirect('record_detail', pk=pk)
    else:
        messages.success(request,"You must be logged in to delete a record")
        return redirect('home')

def record_create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            city = request.POST['city']
            zipcode = request.POST['zipcode']
            record = Record.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                address=address,
                city=city,
                zipcode=zipcode
            )
            messages.success(request,"Record created successfully")
            return redirect('record_detail', pk=record.id)
        else:
            return render(request,'record_create.html')
    else:
        messages.success(request,"You must be logged in to create a record")
        return redirect('home')