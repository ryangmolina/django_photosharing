from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import CharField, TextInput, PasswordInput


class LoginForm(AuthenticationForm):
    username = CharField(label='Username', widget=TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        }
    ))

    password = CharField(label='Password', widget=PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        }
    ))


class SignupForm(UserCreationForm):
    username = CharField(label='Username', widget=TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        }
    ))

    password1 = CharField(label='Password', widget=PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        }
    ))

    password2 = CharField(label='Password confirmation', widget=PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        }
    ))
