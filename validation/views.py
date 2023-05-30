from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def Register(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cPassword = request.POST.get('cpassword')
        if password != cPassword:
            return HttpResponse("Password doesn't match")
        else:
           my_user = User.objects.create_user(username,email,password)
           my_user.save()
           return redirect('login')

    return render(request,'Register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect ('home')
        else:
            return HttpResponse('Email or Password not Correct')
        

    return render(request,'Login.html')
@login_required(login_url='login')
def Home(request):
    return render(request,'home.html')

def Logout(request):
    logout(request) 
    return redirect('login')