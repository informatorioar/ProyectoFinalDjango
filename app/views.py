from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View, UpdateView, DeleteView,ListView
from app.forms import ProductCreateForms,ContactCreateForms,UserRegisterForm,UserEditForm
from app.models import Cliente,Producto,Contacto
from django.urls import reverse_lazy

#AGREGADOS PARA EL LOGIN/LOGOUT
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required

#AGREGADO PARA EL ENVIO DE MAIL
from django.core.mail import EmailMessage
from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


#----------------------------------------------------------------------------------------------

## VISTAS DE CLIENTE
# Vista de Clase que lista los clientes

class ClientListView(ListView):
    def get(self, request):
        clientes = User.objects.all()
        return render(request, 'clientes_list.html', {'clientes': clientes})


#----------------------------------------------------------------------------------------------

## VISTAS DE PRODUCTO
# Vista de Clase que lista los productos
class ProductListView(ListView):
    def get(self,request,*args,**kwargs):
        productos = Producto.objects.all()
        context = {
            'productos':productos
        }
        return render(request,'productos_list.html',context)


# Vista para realizar búsqueda de productos (por articulo)
def SearchProductView(request):
        context = {
        }
        return render(request,'buscar_producto.html',context)


# Vista para mostar productos buscados (por articulo)
def ToFindProductView(request):
        if request.GET["articulo"]:
            articulo = request.GET["articulo"]
            productos = Producto.objects.filter(articulo__icontains=articulo)
            context = {
                'productos': productos,
                'query': articulo
            }
            return render(request,'resultado_buscar_producto.html',context)

        else:
            mensaje = "Por favor introduce un artículo"
        return HttpResponse(mensaje)


# Vista de clase - permite crear un nuevo Producto

class ProductCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = ProductCreateForms()
        return render(request, 'crear_producto.html', {'form': form})

    def post(self, request):
        form = ProductCreateForms(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user  # guardo usuario actual
            producto.save()
            return redirect('app:productos')

        return render(request, 'crear_producto.html', {'form': form})



# Vista de clase que permite modificar (update) nuestro producto

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Producto
    fields = ['articulo', 'seccion', 'descripcion', 'precio_unitario', 'imagen']
    template_name = 'modifcar_producto.html'

    def get_success_url(self):
        return reverse_lazy('app:productos')

    def test_func(self):
        producto = self.get_object()
        return self.request.user == producto.usuario


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Producto
    template_name = 'borrar_producto.html'
    success_url = reverse_lazy('app:productos')

    def test_func(self):
        producto = self.get_object()
        return self.request.user == producto.usuario

#----------------------------------------------------------------------------------------------

## VISTAS DE CONTACTO
# Vista de clase - permite crear un nuevo Contacto
class ContactCreateView(View):
    def get(self,request,*args,**kwargs):
        #parte creada para llamar el contenido en forms.py
        form = ContactCreateForms()
        context={
            'form':form
        }
        return render(request,'contacto.html',context)
    def post(self,request):
        if request.method=="POST":
            form = ContactCreateForms(request.POST)
            if form.is_valid():
                nombre = form.cleaned_data.get('nombre')
                email = form.cleaned_data.get('email')
                telefono = form.cleaned_data.get('telefono')
                asunto = form.cleaned_data.get('asunto')
                mensaje = form.cleaned_data.get('mensaje')

                #AGREGADO PARA ENVIO DE MAIL
                asunto_mail_usuario = 'contacto - lambda3d'
                mensaje_a_usuario = """
                                    Gracias por contactarte con lambda-3D impresiones.
                                    En breve nos comunicaremos para asesorarte en lo que necesites.
                                    Saludos!
                                    """
                contenido_mail_usuario = """
                                            <html>
                                                <head></head>
                                                <body>
                                                    <h2> Hola %s </h2>
                                                    <p>%s</p>
                                                </body>
                                                <footer style="background-color:rgb(186, 228, 164);">
                                                    <h5 style="color: white;">nuestro mail: ✉️ %s</h5>
                                                </footer>
                                            </html>
                                            """ % (nombre, mensaje_a_usuario, settings.EMAIL_HOST_USER)
                mail_a_usuario = EmailMessage(asunto_mail_usuario, contenido_mail_usuario, to=[email])
                mail_a_usuario.content_subtype = "html" # para heredar atributos de formato HTML

                # Si la cuenta de mail HOST se encuetra configurada...
                try:
                    mail_a_usuario.send()
                    msg_alerta = ""

                # caso contrario, enviará el mensaje...
                except:
                    msg_alerta = """
                               Para que la página envíe mail al usuario, se debe configurar cuenta de mail HOST en 'settings.py'.
                               Es decir, completar con datos de cuenta válida:\n
                               'EMAIL_HOST_USER = cuenta de mail válida.'\n
                               'EMAIL_HOST_PASSWORD = contraseña de la cuenta.'
                               """

                c, created = Contacto.objects.get_or_create(nombre=nombre,email=email,telefono=telefono,asunto=asunto,mensaje=mensaje)
                c.save()
                msg = {'mensaje': f'Gracias "{nombre}". Hemos recibido tu mensaje!!. \n{msg_alerta}'}
                return render(request,"resultado_contacto.html",msg)

        context = {
        }
        return render(request,'contacto.html',context)


#------------------------------------------------------------------------------

# VISTAS DE LOGIN
# Vista de función (def) - Login usuarios
def login_request(request):
        if request.method == "POST":
                form = AuthenticationForm(request,data = request.POST)

                if form.is_valid():
                        usuario = form.cleaned_data.get('username')
                        contra = form.cleaned_data.get('password')

                        user = authenticate(username=usuario,password=contra)

                        if user is not None:
                                login(request,user)
                                msg = {"mensaje": f"Bienivenid@ {usuario}."}
                                return render(request,"resultado_login.html",msg)
                        else:
                                msg = {"mensaje": "Error, datos incorrectos."}
                                return render(request,"resultado_login.html",msg)

                else:
                        msg = {"mensaje": "Error, datos incorrectos."}
                        return render(request,"resultado_login.html",msg)

        form = AuthenticationForm()

        return render(request,"login.html",{'form':form})


# Vista para registro de usuario (crear nuevo)
def register(request):
        if request.method == "POST":
                form = UserRegisterForm(request.POST)
                if form.is_valid():
                        username = form.cleaned_data['username']
                        form.save()
                        msg = {'mensaje': f'Usuario "{username}" creado con éxito!!'}
                        return render(request,"resultado_registro.html",msg)

        else:
                form = UserRegisterForm()

        return render(request,'registro.html',{'form':form})


# Vista de editar el perfil
@login_required
def EditProfile(request):

    usuario = request.user

    if request.method == 'POST':

       form = UserEditForm(request.POST)

       if form.is_valid():

            informacion = form.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "index.html")

    else:

        form = UserEditForm(initial={'email': usuario.email})

    return render(request, "editar_perfil.html", {"form": form, "usuario": usuario})

#------------------------------------------------------------------------------

# VISTAS DE "EMPRESA"
# vista de función (def) - Vista de Nosotros, información sobre la tienda
def AboutUsView(request):
        context = {

        }
        return render(request,"nosotros.html",context)

#--------------------
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Comentario
from django.contrib.auth.decorators import login_required
# Vista de detalle del producto

def producto_detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    comentarios = producto.comentarios.order_by('-creado_en')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            # Redirigir a login o mostrar mensaje de error
            return redirect(f'/login/?next=/app/pelicula/{pk}/')  # o la url que uses

        texto = request.POST.get('comentario')
        if texto:
            Comentario.objects.create(producto=producto, texto=texto, usuario=request.user)
            return redirect('app:producto_detalle', pk=pk)

    return render(request, 'producto_detalle.html', {
        'producto': producto,
        'comentarios': comentarios,
    })


#-----------------------
from django.shortcuts import render
from .models import Producto

def productos_list(request):
    orden = request.GET.get('orden', '')  

    productos = Producto.objects.all()  


    if orden == 'fecha_asc':
        productos = productos.order_by('fecha_publicacion')
    elif orden == 'fecha_desc':
        productos = productos.order_by('-fecha_publicacion')
    elif orden == 'alf_asc':
        productos = productos.order_by('articulo')
    elif orden == 'alf_desc':
        productos = productos.order_by('-articulo')

    context = {
        'productos': productos,
        'orden_actual': orden
    }

    return render(request, 'app/productos_list.html', context)




