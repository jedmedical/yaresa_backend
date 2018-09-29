from django import forms
from django.forms import ModelForm

__author__ = 'andrews'


class LoginForm(forms.Form):
    username = forms.CharField(label="username", required=True, max_length=30)
    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label="Remember me", required=False)

#
#
# class SignupsForm(ModelForm):
#
#     class Meta:
#         model = Signup
#         fields = '__all__'
