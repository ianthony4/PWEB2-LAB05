from django.shortcuts import render
from .models import Blogs

# Create your views here.
def myHomeView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"index.html",{})

def createView(request):
    return render(request,"crear.html",{})

def blogView(request):
    losBlogs = Blogs.objects.all()
    print(losBlogs)
    return render(request,"blogs.html",{'losBlogs':losBlogs})

def editView(request):
    return render(request,"editar.html",{})