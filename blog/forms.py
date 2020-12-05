from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Username/Email',
        widget=forms.TextInput(attrs={'autofocus': True})
    )