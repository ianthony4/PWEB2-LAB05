# Esto creara un formulario dinamico a partir de un modelo
from django import forms
from .models import Blogs

class blogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = '__all__'
        
