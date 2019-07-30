from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Printer


class PrinterRegisterForm(forms.ModelForm):
    model = Printer
    fields = '__all__'
    template_name = 'printers/add_printer.html'

#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email']


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']