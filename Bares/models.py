from unittest.util import _MAX_LENGTH
from django.db import models

class Bares(models.Model):

    nombre = models.CharField(max_length = 100)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.email} - {self.telefono}'


class Heladerias(models.Model):

    nombre = models.CharField(max_length = 100)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.email} - {self.telefono}'

class Restaurantes(models.Model):

    nombre = models.CharField(max_length = 100)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.email} - {self.telefono}'

