from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    """User registration starting from inheritance of models UserCreationForm""" 
    first_name = forms.CharField(max_length=30, required=False, label='First Name', help_text='Optional field.')
    last_name = forms.CharField(max_length=30, required=False,label='Last Name', help_text='Optional field.')
    email = forms.EmailField(required=True, help_text='User email to realize the login.')

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2',)