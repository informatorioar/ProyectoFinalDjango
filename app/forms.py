from django import forms
from .models import Producto, Contacto, NuevoUsuario
from django.contrib.auth.forms import UserCreationForm

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# FORM DE PRODUCTO
class ProductCreateForms(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('articulo','seccion','descripcion','precio_unitario','imagen')

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# FORM DE CONTACTO
class ContactCreateForms(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre','email','telefono','asunto','mensaje')

#------------------------------------------------------------------------------------------------------------------------------------------------------------
# FORMULARIO CREADO PARA REGISTRO DE USUARIO
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Correo electrónico")
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput, help_text="Mínimo 8 caracteres.")
    password2 = forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput)
    fecha_nacimiento = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de nacimiento")
    telefono = forms.CharField(required=False, max_length=50, label="Teléfono")

    # Validacion para datos unicos
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if NuevoUsuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado")
        return email.lower()
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username.lower()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = "Nombre de usuario"
        self.fields['username'].widget.attrs.update({'placeholder': 'Ej: juan123'})

        self.fields['email'].widget.attrs.update({'placeholder': 'Ej: juan@mail.com'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Contraseña segura'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirmar contraseña'})
        self.fields['fecha_nacimiento'].widget.attrs.update({'placeholder': 'dd/mm/aaaa'})
        self.fields['telefono'].widget.attrs.update({'placeholder': 'Ej: 3815551234'})

    class Meta:
        model = NuevoUsuario
        fields = ['username', 'email', 'password1', 'password2', 'fecha_nacimiento', 'telefono']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


#------------------------------------------------------------------------------------------------------------------------------------------------------------
# FORMULARIO CREADO PARA EDICION DE USUARIO
class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Correo electrónico")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput, required=False)
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    # Campos personalizados de NuevoUsuario
    fecha_nacimiento = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha de nacimiento')
    telefono = forms.CharField(required=False, max_length=50, label='Teléfono')

    # Validacion de email unico en edicion
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Excluye el email actual del usuario que esta editando
        if NuevoUsuario.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Este correo ya está registrado')
        return email.lower()

    class Meta:
        model = NuevoUsuario
        fields = ['email', 'last_name', 'first_name', 'fecha_nacimiento', 'telefono', 'password1', 'password2']
        labels = {'first_name': 'Nombre', 'last_name': 'Apellido', 'telefono': 'Teléfono'}
        help_texts = {'password1': 'Dejar en blanco para mantener la contraseña actual',
                      'fecha_nacimiento': 'Formato: DD/MM/AAAA'}