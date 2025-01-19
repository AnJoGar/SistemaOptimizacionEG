from django.db import models

# Create your models here.
from django.db import models
class Tramite(models.Model):
    tipo_tramite = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    pais_origen = models.CharField(max_length=100, blank=True, null=True)
    motivo_viaje = models.CharField(max_length=255, blank=True, null=True)
    tipo_visa = models.CharField(max_length=100, blank=True, null=True)
    numero_pasaporte = models.CharField(max_length=50, blank=True, null=True)
    telefono_contacto = models.CharField(max_length=50, blank=True, null=True)
    email_contacto = models.EmailField(blank=True, null=True)
    direccion_contacto = models.CharField(max_length=255, blank=True, null=True)
    lugar_nacimiento = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre



class SolicitudVisa(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    pais_origen = models.CharField(max_length=100)
    motivo_viaje = models.TextField()
    tipo_visa = models.CharField(max_length=100)  # e.g., tourist, student, work, etc.
    fecha_solicitud = models.DateField()  # Date of application
    numero_pasaporte = models.CharField(max_length=50)  # Passport number
    telefono_contacto = models.CharField(max_length=20, blank=True, null=True)  # Contact phone
    email_contacto = models.EmailField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=20, default='Pendiente')
    def __str__(self):
        return f"Visa solicitada por {self.nombre}"

class SolicitudPasaporte(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    fecha_emision = models.DateField()
    telefono_contacto = models.CharField(max_length=20, blank=True, null=True)  # Contact phone
    email_contacto = models.EmailField(max_length=100, blank=True, null=True)  # Contact email
    direccion_contacto = models.CharField(max_length=200, blank=True, null=True)  
    estado = models.CharField(max_length=20, default='Pendiente')
    def __str__(self):
        return f"Pasaporte solicitado por {self.nombre}"

class SolicitudCedula(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=100)  # Place of birth
    telefono_contacto = models.CharField(max_length=20, blank=True, null=True)  # Contact phone
    email_contacto = models.EmailField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=20, default='Pendiente') 
    def __str__(self):
        return f"Cédula solicitada por {self.nombre}"