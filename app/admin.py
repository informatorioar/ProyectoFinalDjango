from django.contrib import admin

from app.models import Cliente, Contacto, Producto

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Contacto)