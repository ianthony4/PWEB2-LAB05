"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Blogs import views


urlpatterns = [
    path('', views.myHomeView, name='Pagina de inicio'),
    path('crear/', views.createView, name='CrearBlog'),
    path('editar/<str:titulo>', views.editView, name='EditarBlog'),
    path('blogs/', views.blogView, name='Blogs'),
    path('eliminar/<str:titulo>', views.eliminar, name='eliminar'),
    path('admin/', admin.site.urls),
]
