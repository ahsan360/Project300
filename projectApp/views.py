from django.db.models.base import Model
from django.shortcuts import render , redirect
from django.views.generic import ListView,DeleteView
from django.http import HttpResponse
from . import models
from django.contrib import messages
from .forms  import UserRegistrationForm,GeeksForm
# Defining a function which
# will receive request and
# perform task depending
# upon function definition

def hello (request) :
    return render ( request,'projectApp/home.html',{'title': 'home'})
def posts (request) : 
    all_post = models.Add.objects.all()
    return render ( request,'projectApp/post.html',{'posts':all_post })

def cpost (request) : 
    
    if request.method == 'POST':
     form = GeeksForm(request.POST)
     if form.is_valid():
        form.save()
        messages.success(request,'post have  created successfully')
        return redirect('/posts') 
          
    else :
         form = GeeksForm(request.POST)
    return render ( request,'projectApp/cpost.html',{'form' : form})
def signin (request) :
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully created')
            return redirect('/hello') 
    else :
        form =  UserRegistrationForm()
    return render ( request,'projectApp/sign.html',{'form' : form})
def login (rsequest) :
    return render ( rsequest,'projectApp/login.html',{'title': 'Log In'})
def index (request) :
    return render ( request,'projectApp/index.html',{'title': 'index'})

def about (request) :
    return HttpResponse("about Geeks")


def contact (request) :
    return HttpResponse("contact Geeks")