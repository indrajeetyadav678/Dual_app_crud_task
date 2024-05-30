from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import RegistrationModel


# Create your views here.

def home(request):
    Context={}
    Context['form']=RegistrationForm
    return render(request, 'app1/home.html', Context)

def insert (request):
    name=request.POST.get('Name')
    email=request.POST.get('Email')
    phone=request.POST.get('Phone')
    photo=request.POST.get('Photo')
    password=request.POST.get('Password')
    emailmatch=RegistrationModel.objects.filter(Email=email)
    if emailmatch:
        msg="Data already exist"
        return render(request, 'app1/home.html')
    else:
        RegistrationModel.objects.create(
            Name= name,
            Email=email,
            Phone=phone,
            Photo=photo,
            Password=password
            )
        msg="Your Data Inserted Successfully"
        return render(request, 'app1/home.html')
    
def show(request):
    data=RegistrationModel.objects.all()
    print(data)
    return render(request, 'app1/home.html', {'key': data})


