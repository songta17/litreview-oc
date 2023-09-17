from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=63,
        widget=forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur'}),
        label=''
    )
    password = forms.CharField(
        max_length=63,
        widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}),
        label=''
    )


class SignupForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur'}),
        label=''
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}),
        label=''
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirmez le mot de passe'}),
        label=''
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Adresse électronique'}),
        label='',
        required=False
    )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Prénom'}),
        label='',
        required=False
    )
    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Nom'}),
        label='',
        required=False
    )
    role = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Rôle'}),
        label='',
        required=False
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username']
        # , 'email', 'first_name', 'last_name', 'role')
        email = forms.EmailField(required=False)
        first_name = forms.CharField(required=False)
        last_name = forms.CharField(required=False)
        role = forms.CharField(required=False)
