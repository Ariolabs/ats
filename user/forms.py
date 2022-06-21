from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class meta:
        model = User
        fields = ["email", "username", "phone_number", "password1", "password2"]