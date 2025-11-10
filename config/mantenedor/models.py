from django.db import models

# Create your models here.
class Cliente(models.Model):
    cargo = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    correo = models.EmailField()
    contacto = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"