from django.contrib import admin
from .models import Producto, Contacto, NuevoUsuario
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# admin.site.register(Cliente) 
admin.site.register(Producto)
admin.site.register(Contacto)

class NuevoUsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'fecha_nacimiento', 'telefono')
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {
            'fields': ('fecha_nacimiento', 'telefono')
        }),
    )

admin.site.register(NuevoUsuario, NuevoUsuarioAdmin)