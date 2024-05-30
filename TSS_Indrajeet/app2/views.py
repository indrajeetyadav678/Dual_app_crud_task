from django.shortcuts import render
from app1.models import*
from app1.forms import RegistrationForm

# Create your views here.
def edit(request, pk):
    data=RegistrationModel.objects.get(id=pk)
    Context={}
    Context['form']=RegistrationForm
    return render(request, 'app1/update.html', {'key': data, 'key1':Context})

def update(request):
    pk=request.POST.get('id')
    data=RegistrationModel.objects.get(id=pk)
    data.Name=request.POST.get('Name')
    data.Email=request.POST.get('Email')
    data.Phone=request.POST.get('Phone')
    data.Photo=request.POST.get('Photo')
    data.Password=request.POST.get('Password')
    data.save()
    data=RegistrationModel.objects.all()
    print(data)
    return render(request, 'app1/home.html', {'key': data})

def delet(request, pk):
    data=RegistrationModel.objects.get(id=pk)
    data.delete()
    data1=RegistrationModel.objects.all()
    return render(request, 'app1/home.html', {'key': data1})