from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=80)
    decripcion = models.TextField(max_length=150)
    texto = models.TextField(max_length=1500)
    imagen = models.ImageField(upload_to='imagenes/')
    fecha = models.DateField()