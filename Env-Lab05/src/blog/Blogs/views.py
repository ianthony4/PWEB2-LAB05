from django.shortcuts import render, redirect
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

def eliminar(request, titulo):
    blog = Blogs.objects.get(titulo=titulo)
    blog.delete()
    return redirect('Blogs')