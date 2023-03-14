from django.db import models

from django.db import models

class Cursos(models.Model):
    Nombre = models.CharField(max_length=50)
    camada = models.IntegerField()
    
class Estudiantes(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
class Profesor(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    email = models.EmailField()
    Materia = models.CharField(max_length=100)
    
class Entregas(models.Model):
    Nombre =  models.CharField(max_length=50)
    fechaDeEntrega = models.DateField()
    Entregado = models.BooleanField()
