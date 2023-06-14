from django.db import models

# Create your models here.
class Persona(models.Model):
    #Opciones para elegir el genero
    GENERO_CHOICES = [
        ('H', 'Hombre'),
        ('M', 'Mujer'),
        ('ND', 'Prefiero no decirlo')
    ]

    #Espacios para el registro de personas
    usuario = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    genero = models.CharField(max_length=2, choices=GENERO_CHOICES)
    ciudad = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    
    # Esto mostrara el usuario en vez de 'persona object'
    def __str__(self):
        return self.usuario