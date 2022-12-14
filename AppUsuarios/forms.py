from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Correo Electrónico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Reingrese el Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserEditForm(UserCreationForm, forms.Form):
    first_name = forms.CharField(max_length=50, label="Nombre")
    last_name = forms.CharField(max_length=50, label="Apellido")
    email = forms.EmailField(label="Correo Electrónico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Reingrese el Password", widget=forms.PasswordInput, required=False)
    

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

        help_text = {"email": "Acá va tu correo electrónico", "first_name": "", "last_name": ""}


class avatarFORM(forms.Form):
    imagen = forms.ImageField()