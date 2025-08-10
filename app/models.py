from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

# Clase Cliente
# class Cliente(models.Model):
#     nombre = models.CharField(max_length=50)
#     apellido = models.CharField(max_length=50)
#     direccion = models.CharField(max_length=100)
#     email = models.EmailField()
#     telefono = models.CharField(max_length=30)

#     def __str__(self) -> str:
#         return f'Nombre: {self.nombre} | Apellido: {self.apellido} | Dirección: {self.direccion} | email: {self.email} | telefono: {self.telefono}'

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# Registro de Usuario

class NuevoUsuario(AbstractUser):
    fecha_nacimiento = models.DateField(blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)

    def get_absolute_url(self):
        return reverse('index')
    
    def __str__(self):
        return self.username
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------

# Clase Producto
class Producto(models.Model):
    GENERO_CHOICES = [
        ('ACC', 'Acción'),
        ('COM', 'Comedia'),
        ('DRA', 'Drama'),
        ('TER', 'Terror'),
        ('SCI', 'Ciencia Ficción'),
        ('FAN', 'Fantasía'),
        ('ROM', 'Romance'),
        ('ANI', 'Animación'),
    ]
    
    articulo = models.CharField('Película', max_length=50)
    seccion = models.CharField('Género', max_length=3, choices=GENERO_CHOICES)
    descripcion = models.TextField('Reseña')
    precio_unitario = models.IntegerField(
        'Puntaje (1-5)',
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Puntaje de 1 a 5 estrellas"
    )
    imagen = models.ImageField('Portada', null=True, blank=True)
    autor = models.ForeignKey(NuevoUsuario, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.autor and hasattr(self, 'request_user'):
            self.autor = self.request_user
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.articulo} ({self.get_seccion_display()}) - {self.precio_unitario}★'
#------------------------------------------------------------------------------------------------------------------------------------------------------------

# Clase Contacto (Feedback Clientes)
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()

    def __str__(self) -> str:
        return f'Mensaje - Asunto: {self.asunto} | Mensaje: {self.mensaje}'

