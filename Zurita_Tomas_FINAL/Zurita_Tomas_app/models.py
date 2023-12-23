from django.db import models

# Create your models here.


class Institucion(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Inscrito(models.Model):
    ESTADOS = (
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO ASISTEN', 'No Asisten'),
    )
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    fechainscripcion = models.DateTimeField(auto_now_add=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    horainscripcion = models.TimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    observacion = models.TextField(blank=True)