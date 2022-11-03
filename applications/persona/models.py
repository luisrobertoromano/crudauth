from django.db import models

# Create your models here.

class Persona(models.Model):
    """Model definition for Persona."""

    apellidos = models.CharField("Apellidos", max_length=50)
    nombres = models.CharField("Nombres", max_length=50)
    dni = models.CharField("DNI", max_length=50)

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        """Unicode representation of Persona."""
        return self.apellidos + ", " + self.nombres

