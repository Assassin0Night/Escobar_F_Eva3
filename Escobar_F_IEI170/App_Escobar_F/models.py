from django.db import models

# Create your models here.
class Inscrito(models.Model):
    
    ESTADOS = [('reservado','RESERVADO'),('completada','COMPLETADA'),('anulada','ANULADA'),('no asisten','NO ASISTEN'),]
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField(max_length=9)
    fecha_inscripcion = models.DateField()
    institucion = models.CharField(max_length=20)
    hora_inscripcion = models.TimeField()
    estado = models.CharField(max_length= 10,choices = ESTADOS)
    observacion = models.TextField(max_length=150)
    
class Institucion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_institucion = models.CharField(max_length=20)