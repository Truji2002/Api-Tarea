from django.db import models

# Create your models here.

class Tarea(models.Model):
    ESTATUS_OPCIONES = [
        ('pendiente', 'Pendiente'),
        ('en progreso', 'En progreso'),
        ('completado', 'Completado'),
    ]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    estatus = models.CharField(
        max_length=15,
        choices=ESTATUS_OPCIONES,
        default='pendiente'
    )

