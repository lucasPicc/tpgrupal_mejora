from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class Bares(models.Model):

    nombre = models.CharField(max_length = 100)
    email = models.EmailField(verbose_name="Correo electrónico")
    telefono = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.email} - {self.telefono}'


class Heladerias(models.Model):

    nombre = models.CharField(max_length = 100)
    email = models.EmailField(verbose_name="Correo electrónico")
    telefono = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.email} - {self.telefono}'

class Restaurantes(models.Model):

    nombre = models.CharField(max_length = 100)
    email = models.EmailField(verbose_name="Correo electrónico")
    telefono = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.email} - {self.telefono}'

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
