from django.db import models
from django.contrib import admin

class Autor(models.Model):
    nombre =   models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()


    def __str__(self):

        return self.nombre

class Libros(models.Model):
    nombre    = models.CharField(max_length=60)
    publicacion      = models.DateField()
    autores   = models.ManyToManyField(Autor, through='Contribuciones')

    def __str__(self):

        return self.nombre

class Contribuciones (models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    libros = models.ForeignKey(Libros, on_delete=models.CASCADE)

class ContribucionesacionInLine(admin.TabularInline):
    model = Contribuciones
    extra = 1

class AutorAdmin(admin.ModelAdmin):
    inlines = (ActuacionInLine,)

class PeliculaAdmin (admin.ModelAdmin):
    inlines = (ContribucionesacionInLine,)

class Meta:
        verbose_name_plural ="libros"
