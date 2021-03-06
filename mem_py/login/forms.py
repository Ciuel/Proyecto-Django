from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import UserProfile

# Create your forms here 

class LoginForm(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(self, request, *args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Nombre de Usuario'})
        self.fields['password'].widget.attrs.update({'placeholder':'Contraseña'})        
        self.error_messages['invalid_login']="Contraseña o Usuario incorrecto"
        for fieldname in ['username','password']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label=""
    class Meta:
        model= UserProfile
        fields=[
            "username",
            "password",
        ]

class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Nombre de Usuario'})
        self.fields['email'].widget.attrs.update({'placeholder':'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Contraseña'})        
        self.fields['password2'].widget.attrs.update({'placeholder':'Repetir Contraseña'})
        self.error_messages["password_mismatch"]="Las contraseñas no coinciden"
        for fieldname in ['username','email','password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label=""

    class Meta:
        model= UserProfile
        fields=[
            "username",
            "email",
            "password1",
            "password2",
        ]
