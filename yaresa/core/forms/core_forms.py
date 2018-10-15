from django import forms
import datetime as base_datetime
__author__ = 'andrews'

Title = (("Mr", "Mr"), ("Mrs", "Mrs"),("Dr", "Dr"))
Sex = (("Male", "Male"), ("Female", "Female"))
Marital_status = (("Single","Single"),("Married","Married"))
Blood_Group = (("A+","A+"),("B+","B+"),("AB+","AB+"),("O+","O+"),("A-","A-"),("B-","B-"),("AB-","AB-"),("O-","O-"))
Sickling_Status = (("AA","AA"),("AS","AS"),("SS","SS"),("SC","SC"))
G6pd = (("Normal","Normal"),("Partial Defect","Partial Defect"),("Partial Defect","Partial Defect"),("Full Defect","Full Defect"))
true_or_false = (("Yes","Yes"),("No","No"))
allergytype = (("Drug Allergy","Drug Allergy"),("Food Allergy","Food Allergy"),("Others","Others"))

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

class NewUserMedicalHistoryForm(forms.Form):
    blood_group = forms.ChoiceField( choices= Blood_Group, required=True,widget=forms.Select(attrs={'class': " mdb-select"}),)
    sickling_status = forms.ChoiceField( choices= Sickling_Status, required=True,widget=forms.Select(attrs={'class': " mdb-select"}),)
    g6pd = forms.ChoiceField( choices= G6pd, required=True,widget=forms.Select(attrs={'class': " mdb-select"}),)
    height = forms.CharField(max_length=255,widget=forms.NumberInput(attrs={'class': "form-control"}),)
    weight = forms.CharField(max_length=255,widget=forms.NumberInput(attrs={'class': "form-control"}),)
    bp = forms.CharField(max_length=255,widget=forms.NumberInput(attrs={'class': "form-control"}),)
    diabetes_mellitus = forms.ChoiceField(choices=true_or_false, widget=forms.RadioSelect(attrs={'class': "form-check-input", }), required=False)
    systematic_hypertension = forms.ChoiceField(choices=true_or_false, widget=forms.RadioSelect(attrs={'class': "form-check-input", }), required=False)
    epilepsy = forms.ChoiceField(choices=true_or_false, widget=forms.RadioSelect(attrs={'class': "form-check-input", }), required=False)
    uterine_fibroid = forms.ChoiceField(choices=true_or_false, widget=forms.RadioSelect(attrs={'class': "form-check-input", }), required=False)
    peptic_ulcer_disease = forms.ChoiceField(choices=true_or_false, widget=forms.RadioSelect(attrs={'class': "form-check-input", }), required=False)

    other_condition = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': "form-control"}),)
    medicine = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), )
    dosage = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': "form-control"}),)
    refill_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                  input_formats=["%Y-%m-%d"])
    allergy_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), )
    allergy_type = forms.ChoiceField( choices= allergytype, required=True,widget=forms.Select(attrs={'class': " mdb-select"}),)
    alcohol = forms.ChoiceField(choices=true_or_false, widget=forms.RadioSelect(
        attrs={'class': "form-check-input", }), required=False)
    smoking = forms.ChoiceField(choices=true_or_false, widget=forms.RadioSelect(
        attrs={'class': "form-check-input", }), required=False)
    surgery_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                  input_formats=["%Y-%m-%d"])
    surgery_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), )


class Addusercondition(forms.Form):
    condition = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': "form-control"}),)


class Adduserallergy(forms.Form):
    allergy_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': "form-control"}),)
    allergy_type = forms.ChoiceField( choices= allergytype, required=True,widget=forms.Select(attrs={'class': " mdb-select"}),)



class Addusermedication(forms.Form):
    medicine = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), )
    dosage = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), )
    refill_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                  input_formats=["%Y-%m-%d"])
