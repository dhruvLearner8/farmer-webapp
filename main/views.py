from django import http
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
#from .models import Comp_detail, Desc
import smtplib
import random
import email.message

def explore(request):
    return render(request,'explore.html')

def register(request):
    if request.method=='POST':

        username=request.POST['username']
        email=request.POST['email']
        choice=request.POST['choice']
        
        p1=request.POST['password']
        p2=request.POST['password_confirm']
        if p1==p2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:

               # obj=User.objects.get(username=username)
                #request.session['comp_user']=obj.id
                user=User.objects.create_user(username=username,password=p1,email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not matchong')
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            obj=User.objects.get(username=username)
            request.session['comp_user']=obj.id
            auth.login(request,user)
            
            return render(request,'index.html')
        else:
            messages.info(request,'invalid credintails')
            return redirect('login')
    else:
        return render(request,'login.html')


def submit(request):
    return render(request,"product.html")

def view1(request):
    return render(request,'view1.html')

# Create your views here.
