from django.db import models

# Create your models here.

class Abogado(models.Model):
    id_abogado = models.IntegerField(primary_key=True)
    categoria_abog = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria_abog


class DatosAbogado(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    nombre_abogado = models.CharField(max_length=15)
    universidad = models.CharField(max_length=20)
    annios_experiencia = models.IntegerField(null=True)
    abogado = models.ForeignKey(Abogado, on_delete=models.CASCADE)
    def __str__(self):
        return self.rut+" "+self.nombre_abogado