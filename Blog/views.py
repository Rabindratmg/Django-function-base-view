from django.shortcuts import render
from django.http import HttpResponse
from . models import Blog
from django.shortcuts import redirect
from .forms import BlogForms
# Create your views here.

def Home(request):
    form = BlogForms()
    blog=Blog.objects.all()
    if request.method=='POST':
        form = BlogForms(request.POST)
        if form.is_valid():
            title= form.cleaned_data['title']
            description = form.cleaned_data['description']
            b=Blog.objects.create(title=title,description=description)
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
     if request.method=='POST':
        if None:
            return "Please Enter the data the data"
        else:
            title= request.POST['title']
            description= request.POST['description']
            Blog.objects.update(title=title,description=description)
            return redirect('/')
     else:
        blog= Blog.objects.get(pk=pk)
        return render(request,'update.html',{'blog':blog})
