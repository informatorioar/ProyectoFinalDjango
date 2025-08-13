from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView, ListView, CreateView
from app.forms import ProductCreateForms, ContactCreateForms, UserRegisterForm, UserEditForm
from app.models import Producto, Contacto, Comentario
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView

#AGREGADOS PARA EL LOGIN/LOGOUT
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

#AGREGADO PARA EL ENVIO DE MAIL
from django.core.mail import EmailMessage
from django.conf import settings

#----------------------------------------------------------------------------------------------

## VISTA PARA REGISTRAR USUARIO
class RegistrarUsuario(CreateView):
    template_name = 'registro.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('app:login')

    def form_valid(self, form):
        response = super().form_valid(form)

        try:
            group = Group.objects.get(name='Registrado')
            self.object.groups.add(group)
            messages.success(self.request, 'Registro exitoso. Puede iniciar sesión.')

        except Group.DoesNotExist:
            messages.warning(self.request, 'Registro exitoso, pero no se pudo asignar grupo.')
        return redirect(self.get_success_url()) 

#----------------------------------------------------------------------------------------------

## VISTA PARA LOGOUT
class LogoutView(LogoutView):
    template_name = 'logout.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, 'Logout exitoso')
        return response

#----------------------------------------------------------------------------------------------

## VISTAS DE CLIENTE
# Vista de Clase que lista los clientes
# class ClientListView(ListView):
#     def get(self,request):
#         clientes = Cliente.objects.all()
#         context = {
#             'clientes':clientes
#         }
#         return render(request,'clientes_list.html',context)

#----------------------------------------------------------------------------------------------

## VISTAS DE PRODUCTO
# Vista de Clase que lista los productos
class ProductListView(ListView):
    model = Producto
    template_name = 'productos_list.html'
    context_object_name = 'productos'

    def get_queryset(self):
        queryset = super().get_queryset()
        genero_seleccionado = self.request.GET.get('genero')

        if genero_seleccionado:
            queryset = queryset.filter(seccion=genero_seleccionado)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generos'] = Producto.GENERO_CHOICES
        context['genero_seleccionado'] = self.request.GET.get('genero') 
        return context


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
@method_decorator(login_required, name='dispatch')
class ProductCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ProductCreateForms()
        context = {
            'form': form
        }
        return render(request, 'crear_producto.html', context)
    
    def post(self, request):
        if request.method == "POST":
            form = ProductCreateForms(request.POST, request.FILES)
            if form.is_valid():
                # Crear instancia sin guardar aún
                producto = form.save(commit=False)
                # Asignar el usuario actual como autor
                producto.autor = request.user
                # Ahora guardar en la base de datos
                producto.save()
                
                messages.success(request, 'Post creado exitosamente!')
                return redirect('app:productos')

        context = {
            'form': form
        }
        return render(request, 'crear_producto.html', context)


# Vista de clase que permite modificar (update) nuestro producto
class ProductUpdateView(UpdateView):
    model = Producto
    fields = ['articulo','seccion','descripcion','precio_unitario','imagen']
    template_name = 'modifcar_producto.html'

    def dispatch(self, request, *args, **kwargs):
        producto = self.get_object()
        if not (request.user.is_superuser or request.user == producto.autor):
            raise PermissionDenied('No tienes permiso para editar este post')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('app:productos')


# Vista de clase que nos permite eliminar un producto
class ProductDeleteView(DeleteView):
    model = Producto
    template_name = 'borrar_producto.html'
    success_url = reverse_lazy('app:productos')

    def dispatch(self, request, *args, **kwargs):
        producto = self.get_object()
        if not (request.user.is_superuser or request.user == producto.autor):
            raise PermissionDenied('No tienes permiso para eliminar este post')
        return super().dispatch(request, *args, **kwargs)

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
# def register(request):
#         if request.method == "POST":
#                 form = UserRegisterForm(request.POST)
#                 if form.is_valid():
#                         username = form.cleaned_data['username']
#                         form.save()
#                         msg = {'mensaje': f'Usuario "{username}" creado con éxito!!'}
#                         return render(request,"resultado_registro.html",msg)

#         else:
#                 form = UserRegisterForm()

#         return render(request,'registro.html',{'form':form})


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


#------------------------------------------------------------------------------

# Vista para comentario
@login_required
def agregar_comentario(request, producto_id):
    producto = get_object_or_404(Producto, id = producto_id)
    if request.method == 'POST':
        texto = request.POST.get('texto')
        Comentario.objects.create(
            usuario = request.user,
            texto = texto,
            producto = producto
        )
        return redirect('app:productos')
    return render(request, 'agregar_comentario.html', {'producto' : producto})