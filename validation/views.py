from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core import validators
import re


# Create your views here.

@never_cache
def Register(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cPassword = request.POST.get('cpassword') 
        print('value get')    
        try:
            if len(username)<3:
                raise ValueError('Username should have atleast 3 characters')
            if re.match(r'^[0-9]',username):
                raise ValueError('username should not start with a number')
        except ValueError as msg:
            print('first except')
            messages.error(request,msg)
        else:
            try:
                validators.validate_email(email)  
            except validators.ValidationError:
                messages.error(request,'Invalid Email Address')   
            else:
                if len(password)<8:
                    messages.error(request,'Password should be atleast 8 characters')
                elif password!=cPassword:
                    messages.error(request,"Password Doesn't match")     
                else:
                    try:
                        User.objects.get(username=username)
                        messages.error(request,'Username Already Exist')
                    except User.DoesNotExist:
                        try:
                            User.objects.get(email=email)
                            messages.error(request,'Email Already exist')
                        except User.DoesNotExist:
                            my_user = User.objects.create(username=username,email=email)
                            my_user.password = make_password
                            my_user.save()
                            messages.success(request,'User Registerion Succesfull...')              
                            return redirect('login')
                                  
    return render(request, 'Register.html')

@never_cache
def Login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print('hii')
            return redirect ('home')
        else:
            messages.error(request,'Username or Password not Correct')
         
    return render(request,'Login.html')
        
        


@login_required(login_url='login')
@never_cache
def Home(request): 
    return render(request,'home.html')

def Logout(request):
    logout(request) 
    return redirect('login')