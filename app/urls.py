from django.urls import path
from .views import *

# AGERGADO PARA EL LOGOUT
from django.contrib.auth.views import LogoutView

app_name = 'app'

urlpatterns = [
    
    # path('clientes/',ClientListView.as_view(),name="clientes"),
    path('productos/',ProductListView.as_view(),name="productos"),
    path('buscar_producto/',SearchProductView,name="buscar_producto"),
    path('producto_buscado/',ToFindProductView,name='producto_buscado'),
    path('crear_producto/',ProductCreateView.as_view(),name="crear_producto"),
    path('contacto/',ContactCreateView.as_view(),name="contacto"),
    path('<int:pk>/modificar/',ProductUpdateView.as_view(),name="modificar_producto"),
    path('<int:pk>/delete/',ProductDeleteView.as_view(),name="borrar_producto"),
    path('login',login_request,name="login"),                                           
    path('registro/', RegistrarUsuario.as_view(), name="registro"),                                          
    path('editar_perfil', EditProfile,name="editar_perfil"),                    
    path('logout/', LogoutView.as_view(next_page='app:login'), name="logout"),                          
    path('nosotros/',AboutUsView,name="nosotros"),                              

    
]

