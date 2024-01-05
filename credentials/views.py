from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import auth, messages
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
            
            if not any(messages.get_messages(request)):
                user = User.objects.create(username=username, password=password)
                user.set_password(password)
                user.save()
                return redirect('credentials:login')
        else:
            messages.info(request,'Passwords do not match.')
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(request,username=username,password=password)
        
        if user is not None:
            auth_login(request,user)
            messages.success(request,'Login Succesfull')
            return redirect('bank:connect')
        else:
            messages.error(request,'Invalid Credentials')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('bank:home')
        
