from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User  # <-- Importa User
from datetime import datetime


# Clase Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} | Apellido: {self.apellido} | Dirección: {self.direccion} | email: {self.email} | telefono: {self.telefono}"

# ------------------------------------------------------------------------------

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Producto(models.Model):
    GENERO_CHOICES = [
        ("ACC", "Acción"),
        ("COM", "Comedia"),
        ("DRA", "Drama"),
        ("TER", "Terror"),
        ("SCI", "Ciencia Ficción"),
        ("FAN", "Fantasía"),
        ("ROM", "Romance"),
        ("ANI", "Animación"),
    ]

    articulo = models.CharField("Película", max_length=50)
    seccion = models.CharField("Género", max_length=3, choices=GENERO_CHOICES)
    descripcion = models.TextField("Reseña")
    precio_unitario = models.IntegerField(
        "Puntaje (1-5)",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Puntaje de 1 a 5 estrellas",
    )
    imagen = models.ImageField("Portada", null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='productos', null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.articulo} ({self.get_seccion_display()}) - {self.precio_unitario}★"

# ------------------------------------------------------------------------------

# Clase Contacto (Feedback Clientes)
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()

    def __str__(self) -> str:
        return f"Mensaje - Asunto: {self.asunto} | Mensaje: {self.mensaje}"

# ------------------------------------------------------------------------------

class Comentario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios', null=True, blank=True)

    def __str__(self):
        return f'Comentario en {self.producto.articulo} - {self.creado_en}'



