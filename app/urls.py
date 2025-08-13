# AGERGADO PARA EL LOGOUT
from django.contrib.auth.views import LogoutView, LoginView as auth_views_LoginView
from django.urls import path
from . import views

from app.views import *

# Import productos_list if it's defined elsewhere, otherwise define it in views.py
try:
    from app.views import productos_list
except ImportError:
    pass  # productos_list should be defined in app/views.py

app_name = "app"

urlpatterns = [
    path("clientes/", ClientListView.as_view(), name="clientes"),
    path("productos/", ProductListView.as_view(), name="productos"),
    path("buscar_producto/", SearchProductView, name="buscar_producto"),
    path("producto_buscado/", ToFindProductView, name="producto_buscado"),
    path("crear_producto/", ProductCreateView.as_view(), name="crear_producto"),
    path("contacto/", ContactCreateView.as_view(), name="contacto"),
    path("<int:pk>/modificar/", ProductUpdateView.as_view(), name="modificar_producto"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="borrar_producto"),
    path("registro", register, name="registro"),
    path("editar_perfil", EditProfile, name="editar_perfil"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("nosotros/", AboutUsView, name="nosotros"),
    path('pelicula/<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('login/', auth_views_LoginView.as_view(template_name='login.html'), name='login'),
]


