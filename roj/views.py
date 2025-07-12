from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages   

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=='POST':
        name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=name).exists():
                messages.info(request,"Username alreay exits")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email alreay exits")
                return redirect('register')                
            else:
                user=User.objects.create_user(username=name,email=email,password=password1)
                user.save()
                messages.success(request,'Registration succesful')
                return redirect('index')
        else:
            messages.info(request,'passowrd didnot matched')
            return redirect('register')
    else:
        return render(request,"register.html")

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            messages.success(request,'Login Succesfull')
            return redirect('index')
        else:
            messages.error(request,"login unsucceful")
            return redirect('login')
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('index')

