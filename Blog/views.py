from django.shortcuts import render
from django.http import HttpResponse
from . models import Blog
from django.shortcuts import redirect
from .forms import BlogForms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
# Create your views here.

def Home(request):
    form = BlogForms()
    blog=Blog.objects.all()
    if request.method=='POST':
        form = BlogForms(request.POST)
        if form.is_valid():
            title= form.cleaned_data['title']
            description = form.cleaned_data['description']
            author= form.cleaned_data['author']
            b=Blog.objects.create(title=title,description=description,author=author)
            b.save()
            return render(request,'index.html',{'blogs':blog, 'form':form})

        else:
            return 'enter correct data'
            
            

    return render(request,'index.html',{'blogs':blog ,'form':form})

def BlogDetail(request,pk):
    blog=Blog.objects.get(pk=pk)
    return render(request,'details.html',{'blog':blog})


def BlogDelete(request,pk):
    blog=Blog.objects.get(pk=pk)
    blog.delete()
    return redirect('/')

def BlogUpdate(request,pk):
    form=BlogForms()
    if request.method=='POST':
        form = BlogForms(request.POST)
        if form.is_valid():
            title= form.cleaned_data['title']
            description = form.cleaned_data['description']
            author= form.cleaned_data['author']
            b=Blog.objects.create(title=title,description=description,author=author)
            b.save()
            return redirect('/')
    else:
        blog= Blog.objects.get(pk=pk)
        return render(request,'update.html',{'blog':blog,'form':form})


def usercreation(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')

    return render(request,'register.html',{'form':form})
