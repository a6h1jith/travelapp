from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def second(request):
    if request.method=='POST':
        name=request.POST['name']
        user=request.POST['username']
        Email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=user).exists():
                messages.info(request,"username taken")
                return redirect('/myapp/register')
            elif User.objects.filter(email=Email).exists():
                messages.info(request, "Email aready registered")
                return redirect('/myapp/register')
            else:
                newuser=User.objects.create_user(first_name=name, username=user, email=Email, password=password)
                newuser.save()
                return redirect('/myapp/login')
        else:
            messages.info(request,"Passwords do not match")
        print("User created")

    return render(request,'reg.html')

def login(request):
    if request.method=='POST':
        user1=request.POST['username']
        password=request.POST['password']
        log=auth.authenticate(username=user1, password=password)
        if log is not None:
            auth.login(request,log)
            return redirect('/')
        else:
            messages.info(request,'invalid username or password')
            return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')