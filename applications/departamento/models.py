from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.



class Departamento(models.Model):
    name = models.CharField("Nombre", max_length=50)
    shor_name = models.CharField("Nombre corto", max_length=20)
    active = models.BooleanField("Anulado", default=False)

    #Personalizar nuestro modelo
    class Meta:
        verbose_name='Mi Departamento'
        verbose_name_plural = 'Áreas de la Empresa'
        ordering = ['name']
        #ordering = ['-name'] 
        #esta linea de codigo no permite que se creen dos registros iguales, dependiendo de la combiancion de los campos
        unique_together = ('name','shor_name')

    def __str__ (self):
        return self.name
