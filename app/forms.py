from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.models import Contacto, Producto

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


class ProductCreateForms(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ("articulo", "seccion", "descripcion", "precio_unitario", "imagen")
        widgets = {
            'seccion': forms.Select(attrs={'class': 'form-select'}),
        }


# ------------------------------------------------------------------------------------------------------------------------------------------------------------


# FORM DE CONTACTO
class ContactCreateForms(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ("nombre", "email", "telefono", "asunto", "mensaje")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# FORMULARIO CREADO PARA REGISTRO DE USUARIO
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repita su contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # Saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}


# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# FORMULARIO CREADO PARA EDICION DE USUARIO
class UserEditForm(UserCreationForm):
    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Repetir la contraseña", widget=forms.PasswordInput
    )

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "last_name", "first_name"]

#----------------------------

from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

#----------------------

from django.views import View
from django.shortcuts import render, redirect

class ProductCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ProductCreateForms()
        print(form.fields['seccion'].widget)  # <-- para verificar que es un Select
        context = {'form': form}
        return render(request, 'crear_producto.html', context)

    def post(self, request):
        form = ProductCreateForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:productos')
        context = {'form': form}
        return render(request, 'crear_producto.html', context)
