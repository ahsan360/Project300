from django.db.models.base import Model
from django.shortcuts import render, redirect,reverse 
from django.views.generic import ListView, DeleteView, UpdateView
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from . import models
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from .forms import UserRegistrationForm, GeeksForm, comment
# Defining a function which
 
# will receive request and
# perform task depending
# upon function definition


def hello(request):
    return render(request, 'projectApp/home.html', {'title': 'home'})


@login_required(login_url='/log')
def posts(request):
    all_post = models.Add.objects.all()
    return render(request, 'projectApp/post.html', {'posts': all_post})


def cpost(request):

    if request.method == 'POST':
     form = GeeksForm(request.POST)
     if form.is_valid():
        form.save()
        messages.success(request, 'post have  created successfully')
        return redirect('/posts')

    else:
         form = GeeksForm(request.POST)
    return render(request, 'projectApp/cpost.html', {'form': form})


def signin(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully created')
            return redirect('/hello')
    else:
        form = UserRegistrationForm()
    return render(request, 'projectApp/sign.html', {'form': form})


def log(request):
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, username=username, password=password)
         if user is not None:
             login(request, user)
             return redirect('/hello')
         else:
            return redirect('/log')
    else:
        return render(request, 'projectApp/log.html', {'title': 'Log In'})


def index(request):
    return render(request, 'projectApp/index.html', {'title': 'index'})


def details(request, id):

    obj = get_object_or_404(models.Add, pk=id)
    all_post = models.Add.objects.all()
    return render(request, 'projectApp/details.html', {'posts': all_post, 'obj': obj, })

def addcomment(request,pk):
  eachProduct = models.Add.objects.get(id=pk)
  cot = models.Hello.objects.filter(pk=pk).last()
  form = comment(instance=eachProduct)
  if request.method == 'POST':
     form = comment(request.POST, instance=eachProduct)
     form = comment(request.POST, request.FILES)
     if form.is_valid():
        name = request.user.username
        body = form.cleaned_data['body']
        img =  form.cleaned_data.get('image')
        c =  models.Hello(name=name,image=img ,post= eachProduct, body=body, date_added=datetime.now())
        c.save()
        messages.success(request,'comment successfully')
        return redirect('details',id = pk)
         
        
  else :
         form = comment(request.POST)
  return render(request, 'projectApp/addcomment.html',{'form': form})

def about (request) :
    return HttpResponse("about Geeks")
def search (request) :
    if request.method == 'GET':
        search = request.GET.get('search')
        post = models.Add.objects.all().filter(title=search)
    return render ( request,'projectApp/search.html',{'post':post})

def contact (request) :
    return HttpResponse("contact Geeks")
def Update (request,pk) :
    pk  = models.Add.objects.get(pk=pk)
    if request.method == 'POST':
     form = GeeksForm(request.POST,instance=pk)
     if form.is_valid():
        form.save()
        messages.success(request,'post have  Updated successfully')
        return redirect('/posts') 
          
    else :
         form = GeeksForm(instance=pk)
         return render ( request,'projectApp/Update.html',{'form' : form})
def delete (request,pk) :
    info  = models.Add.objects.get(pk=pk)
    info.delete()
    messages.success(request,'post have  Deleted successfully')
    return redirect('/posts')

def delete_comment(request, pk):
    comment = models.Hello.objects.filter(pk=pk).last()
    product_id = comment.post.id
    comment.delete()
    return redirect('details', id=comment.post.id)
   
