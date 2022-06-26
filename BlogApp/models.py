from operator import truediv
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User


class BlogModel(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to = "imagenes", null=True, blank=True)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.titulo} ({self.subtitulo}) - {self.autor} en {self.creacion}'
