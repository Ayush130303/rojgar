from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib import messages   
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator
# Create your views here.
from .models import Job
def index(request):
    if request.user.is_authenticated:
        search=None
        if request.method=='POST':
            search=request.POST.get('search','').strip()
            jobs=Job.objects.filter(title__icontains=search)
        else:
            jobs = Job.objects.all().order_by("external_id") 
        paginator = Paginator(jobs, 6)
        page_obj = paginator.get_page(request.GET.get('page'))

        return render(request, "index.html", {
            'jobs': page_obj.object_list,  # optional
            'page': page_obj,
            'search':search

        })

    return render(request, "index.html")  # for not-logged-in users


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

User=get_user_model()
def user_login(request):
    if request.method=='POST':
        identity=request.POST['username']
        password=request.POST['password']
        if '@' in identity:
            try:
                identity = User.objects.get(email__iexact=identity).username
            except User.DoesNotExist:
                messages.error(request, "Invalid email or password.")
                return redirect('login')

        user=authenticate(request,username=identity,password=password)

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

@login_required

def profile(request):
    # job=Job.objects.all()
    return render(request,'profile.html')