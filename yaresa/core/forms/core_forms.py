from django import forms
import datetime as base_datetime
__author__ = 'andrews'

Title = (("Mr", "Mr"), ("Mrs", "Mrs"),("Dr", "Dr"))
Sex = (("Male", "Male"), ("Female", "Female"))
Marital_status = (("Single","Single"),("Married","Married"))
Blood_Group = (("A+","A+"),("B+","B+"),("AB+","AB+"),("O+","O+"),("A-","A-"),("B-","B-"),("AB-","AB-"),("O-","O-"))
Sickling_Status = (("AA","AA"),("AS","AS"),("SS","SS"),("SC","SC"))
G6pd = (("Normal","Normal"),("Partial Defect","Partial Defect"),("Partial Defect","Partial Defect"),("Full Defect","Full Defect"))

class NewUserForm(forms.Form):
    picture = forms.ImageField()
    title = forms.ChoiceField( choices= Title, required=True,widget=forms.Select(attrs={'class': " mdb-select"}),)
    first_name = forms.CharField(max_length=255 ,widget=forms.TextInput(attrs={'class': "form-control"}),)
    other_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': "form-control"}),)

    surname = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': "form-control"}),)
    sex = forms.ChoiceField(choices=Sex, widget=forms.RadioSelect(attrs={'class': "form-check-input", }), required=False)

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                  input_formats=["%Y-%m-%d"])
    nationality = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': "form-control"}),)
    religion = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': "form-control"}),)
    marital_status = forms.ChoiceField(choices=Marital_status, widget=forms.RadioSelect(attrs={'class': "form-check-input", }), required=False)
    address = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': "form-control"}),)
    occupation = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': "form-control"}),)
    email = forms.EmailField(max_length=255,widget=forms.TextInput(attrs={'class': "form-control"}),)
    mobile = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': "form-control"}),)
    emergency_contact_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': "form-control"}),)
    emergency_contact_mobile = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': "form-control"}),)
    blood_group = forms.ChoiceField( choices= Blood_Group, required=True,widget=forms.Select(attrs={'class': " mdb-select"}),)
    sickling_status = forms.ChoiceField( choices= Sickling_Status, required=True,widget=forms.Select(attrs={'class': " mdb-select"}),)
    g6pd = forms.ChoiceField( choices= G6pd, required=True,widget=forms.Select(attrs={'class': " mdb-select"}),)

