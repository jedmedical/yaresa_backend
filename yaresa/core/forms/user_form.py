from django import forms
from django.forms import ModelForm

__author__ = 'andrews'


class LoginForm(forms.Form):
    username = forms.CharField(label="username", required=True, max_length=30,widget=forms.TextInput(attrs={'class': "form-control"}),)
    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput(attrs={'class': "form-control"}),)
    remember_me = forms.BooleanField(label="Remember me", required=False)

#
#
# class SignupsForm(ModelForm):
#
#     class Meta:
#         model = Signup
#         fields = '__all__'


class NewAdminUserForm(forms.Form):
    first_name = forms.CharField(label="first name", required=True, max_length=30,widget=forms.TextInput(attrs={'class': "form-control"}),)
    last_name = forms.CharField(label="last name", required=True, max_length=30,widget=forms.TextInput(attrs={'class': "form-control"}),)
    email = forms.CharField(label="username", required=True, max_length=30, widget=forms.TextInput(attrs={'class': "form-control"}),)
    user_type = forms.CharField(label="Password", required=True, widget=forms.PasswordInput(attrs={'class': "form-control"}),)

