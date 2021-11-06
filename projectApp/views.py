from django.db.models.base import Model
from django.shortcuts import render , redirect
from django.views.generic import ListView,DeleteView
from django.http import HttpResponse
from . import models
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms  import UserRegistrationForm,GeeksForm
# Defining a function which
# will receive request and
# perform task depending
# upon function definition

def hello (request) :
    return render ( request,'projectApp/home.html',{'title': 'home'})


@login_required(login_url='/log') 
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
    
def log (request) :
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, username=username, password=password)
         if user is not None:
             login(request, user)
             return redirect('/hello')
         else:
            return redirect('/log')
    else :
        return render ( request,'projectApp/log.html',{'title': 'Log In'})
def index (request) :
    return render ( request,'projectApp/index.html',{'title': 'index'})
def details (request,id) :
    all_post = models.Add.objects.all()
    obj = get_object_or_404(models.Add, pk=id)
    return render ( request,'projectApp/details.html',{'posts': all_post,'obj': obj})
def about (request) :
    return HttpResponse("about Geeks")
def search (request) :
    if request.method == 'GET':
        search = request.GET.get('search')
        post = models.Add.objects.all().filter(title=search)
    return render ( request,'projectApp/search.html',{'post':post})

def contact (request) :
    return HttpResponse("contact Geeks")