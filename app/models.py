from django.db import models

# Create your models here.

# Clase Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'Nombre: {self.nombre} | Apellido: {self.apellido} | Dirección: {self.direccion} | email: {self.email} | telefono: {self.telefono}'

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# Clase Producto
class Producto(models.Model):
    articulo = models.CharField(max_length=50)
    seccion = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio_unitario = models.IntegerField()
    imagen = models.ImageField(null=True,blank=True)

    def __str__(self) -> str:
        return f'Artículo: {self.articulo} | Sección: {self.seccion} | P.unit.: ${self.precio_unitario}'

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

#------------------------------------------------------------------------------------------------------------------------------------------------------------
