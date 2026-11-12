from django.db import models

# Create your models here.


class Carrera(models.Model):
    nombre = models.CharField(max_length=128)
    
    def __str__(self):
        return self.nombre
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    mostrar = models.CharField(max_length=256)
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Materia(models.Model):
    nombre = models.CharField(max_length=128)
    cant_alumnos = models.IntegerField(default=5)
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Aula(models.Model):
    descripcion = models.CharField(max_length=128)
    ubicacion = models.CharField(max_length=128)
    cant_proyector = models.IntegerField(default=0)
    aforo = models.IntegerField(default=0)
    es_climatizada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.descripcion