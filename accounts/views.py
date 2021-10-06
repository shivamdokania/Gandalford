from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
            if User.objects.filter(username=email).exists():
                messages.info(request,'User exists')
                return render(request,'Register.html')
            else:
                user=User.objects.create_user(username=email,password=password1,email=email,first_name=name)
                user.save()
                messages.info(request,'User Created')
                return redirect('login')
        else:
            messages.info(request,'Password Not Matching')
            return render(request,'Register.html')

    return render(request,'Register.html')

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password1')
        user=auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    

    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')