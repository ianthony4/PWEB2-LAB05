from django.db import models

# Create your models here.
class Blogs(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=10000)

    # Esto mostrara el nombre del blog por titulo, y no como "object blog"
    def __str__(self):
        return self.titulo