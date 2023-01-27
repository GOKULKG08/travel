from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username= request.POST.get("username")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('password1')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info (request,'user taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user= User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                print ('user created')
                return  redirect('login')

        else:
             messages.info(request,'password not matching')
             return redirect('register')
             return redirect('/')

    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

