from django.contrib import admin
from .models import Producto, Contacto, NuevoUsuario, Comentario
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

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'texto', 'fecha_creacion', 'activo')
    list_filter = ('activo', 'fecha_creacion')
    search_fields = ('texto', 'usuario__username')

admin.site.register(Comentario, ComentarioAdmin)