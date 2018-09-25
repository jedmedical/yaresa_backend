from core.models.biostatistics import Biostatistic
from core.models.med_graphic import Med_graphic
from core.models.signups import Signup
from django import forms
from django.forms import ModelForm

__author__ = 'andrews'


class LoginForm(forms.Form):
    phone = forms.CharField(label="phone", required=True, max_length=30)
    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label="Remember me", required=False)



class SignupsForm(ModelForm):

    class Meta:
        model = Signup
        fields = '__all__'
