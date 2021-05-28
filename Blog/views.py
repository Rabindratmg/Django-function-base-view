from django.shortcuts import render
from django.http import HttpResponse
from . models import Blog
from django.shortcuts import redirect
# Create your views here.

def Home(request):
    blog=Blog.objects.all()
    if request.method=='POST':
        if None:
            return "Please Enter the data the data"

        else:
            title= request.POST['title']
            description= request.POST['description']
            b=Blog.objects.create(title=title,description=description)
            b.save()
            return render(request,'index.html',{'blogs':blog})
            

    return render(request,'index.html',{'blogs':blog})

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
