from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"index.html",{})

def createView(request):
    return render(request,"crear.html",{})

def editView(request):
    return render(request,"editar.html",{})