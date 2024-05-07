from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employe

# Create your views here.
def hello(request):
    return HttpResponse("hello employee")

def register(request):
    if request.method == "POST":
        Name = request.POST['name']
        Si = request.POST['si']
        Age = request.POST['age']
        Income = request.POST['income']
        Username = request.POST['username']
        Password = request.POST['password']
        Image = request.FILES['image']
        employe = Employe.objects.create(name=Name,si=Si,age=Age,income=Income,username=Username,password=Password,image=Image)
        employe.save()
        return HttpResponse("COMPLETED")
    else:    
        return render(request,'registration.html')
    
def login(request):
    if request.method == "POST":
        Username = request.POST['username']
        Password = request.POST['password']
        try:
            data = Employe.objects.get(username=Username) ##data is an object of class Employe.so data can acsess 
            if data.password == Password :                ##Employe's attributes 
                request.session['id'] = data.id
                return redirect(profile)   ##return HttpResponse("login sucessfully")
            else:
                return HttpResponse("incorrect password")
        except:
            return HttpResponse("username error")
    else:
        return render(request,'login.html')

def profile(request):
    if 'id' in request.session:
        Id = request.session['id']
        data = Employe.objects.get(id=Id)
        return render(request,'profile.html',{'data':data})
    else:
        return HttpResponse("user not loged in")

def logout(request):
    if 'id' in request.session :
        request.session.flush() 
        return redirect(login)