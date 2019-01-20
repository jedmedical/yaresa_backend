from django import forms
import datetime as base_datetime
__author__ = 'andrews'

Title = (("Mr", "Mr"), ("Mrs", "Mrs"),("Dr", "Dr"))
Sex = (("Male", "Male"), ("Female", "Female"))
Marital_status = (("Single","Single"),("Married","Married"))
Blood_Group = (("A+","A+"),("B+","B+"),("AB+","AB+"),("O+","O+"),("A-","A-"),("B-","B-"),("AB-","AB-"),("O-","O-"))
Sickling_Status = (("AA","AA"),("AS","AS"),("SS","SS"),("SC","SC"))
G6pd = (("Normal","Normal"),("Partial Defect","Partial Defect"),("Full Defect","Full Defect"))
true_or_false = (("Yes","Yes"),("No","No"))
allergytype = (("Drug Allergy","Drug Allergy"),("Food Allergy","Food Allergy"),("Others","Others"))

class NewUserForm(forms.Form):
    picture = forms.ImageField()
    title = forms.ChoiceField( choices= Title, required=True,widget=forms.Select(attrs={'class': " mdb-select"}),)
    first_name = forms.CharField(max_length=255 ,widget=forms.TextInput(attrs={'class': "form-control"}),)
    other_name = forms.CharField(max_length=255, required=False,widget=forms.TextInput(attrs={'class': "form-control"}),)

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
    height = forms.CharField(max_length=255,widget=forms.NumberInput(attrs={'class': "form-control",'oninput':"your_bmi()"}),)
    weight = forms.CharField(max_length=255,widget=forms.NumberInput(attrs={'class': "form-control",'oninput':"your_bmi()"}),)

    systolic =  forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': "form-control bpressure", "oninput":"your_bp()"}),)

    diastolic =  forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': "form-control bpressure","oninput":"your_bp()"}),)

    diabetes_mellitus = forms.ChoiceField(choices=true_or_false, widget=forms.RadioSelect(attrs={'class': "form-check-input", }), required=False)
    systematic_hypertension = forms.ChoiceField(choices=true_or_false, widget=forms.RadioSelect(attrs={'class': "form-check-input", }), required=False)
    epilepsy = forms.ChoiceField(choices=true_or_false, widget=forms.RadioSelect(attrs={'class': "form-check-input", }), required=False)
    uterine_fibroid = forms.ChoiceField(choices=true_or_false, widget=forms.RadioSelect(attrs={'class': "form-check-input", }), required=False)
    peptic_ulcer_disease = forms.ChoiceField(choices=true_or_false, widget=forms.RadioSelect(attrs={'class': "form-check-input", }), required=False)

    other_condition = forms.CharField(max_length=255,required=False,widget=forms.TextInput(attrs={'class': "form-control"}),)
    other_condition_1 = forms.CharField(max_length=255, required=False,
                                      widget=forms.TextInput(attrs={'class': "form-control"}), )
    other_condition_2 = forms.CharField(max_length=255, required=False,
                                      widget=forms.TextInput(attrs={'class': "form-control"}), )
    other_condition_3 = forms.CharField(max_length=255, required=False,
                                      widget=forms.TextInput(attrs={'class': "form-control"}), )
    medicine = forms.CharField(max_length=255, required=False,widget=forms.TextInput(attrs={'class': "form-control"}), )
    dosage = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': "form-control"}),)
    refill_date = forms.DateField( required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                  input_formats=["%Y-%m-%d"])

    medicine_1 = forms.CharField(max_length=255, required=False,
                               widget=forms.TextInput(attrs={'class': "form-control"}), )
    dosage_1 = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': "form-control"}), )
    refill_date_1 = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                  input_formats=["%Y-%m-%d"])
    medicine_2 = forms.CharField(max_length=255, required=False,
                                 widget=forms.TextInput(attrs={'class': "form-control"}), )
    dosage_2 = forms.CharField(max_length=255, required=False,
                               widget=forms.TextInput(attrs={'class': "form-control"}), )
    refill_date_2 = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                    input_formats=["%Y-%m-%d"])

    allergy_name = forms.CharField( required=False,max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), )
    allergy_type = forms.ChoiceField( required=False, choices= allergytype, widget=forms.Select(attrs={'class': " mdb-select"}),)

    allergy_name_1 = forms.CharField(required=False, max_length=255,
                                   widget=forms.TextInput(attrs={'class': "form-control"}), )
    allergy_type_1 = forms.ChoiceField(required=False, choices=allergytype,
                                     widget=forms.Select(attrs={'class': " mdb-select"}), )
    allergy_name_2 = forms.CharField(required=False, max_length=255,
                                   widget=forms.TextInput(attrs={'class': "form-control"}), )
    allergy_type_2 = forms.ChoiceField(required=False, choices=allergytype,
                                     widget=forms.Select(attrs={'class': " mdb-select"}), )

    alcohol = forms.ChoiceField( choices=true_or_false, widget=forms.RadioSelect(
        attrs={'class': "form-check-input", }), )
    smoking = forms.ChoiceField(choices=true_or_false, widget=forms.RadioSelect(
        attrs={'class': "form-check-input", }), )
    surgery_date = forms.DateField( required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                  input_formats=["%Y-%m-%d"])
    surgery_name = forms.CharField( required=False,max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), )
    surgery_doctor = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), )
    surgery_hospital = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control"}), )

    surgery_date_1 = forms.DateField( required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                  input_formats=["%Y-%m-%d"])
    surgery_name_1 = forms.CharField( required=False,max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), )
    surgery_doctor_1 = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control"}), )
    surgery_hospital_1 = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control"}), )
    fbs_test_result = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control",'oninput':"your_fbs()"}),)
    fbs_test_date = forms.DateField( required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                  input_formats=["%Y-%m-%d"])
    next_fbs_test = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                    input_formats=["%Y-%m-%d"])
    fbs_saved_result = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'id':"fbs",'disabled':"true", 'placeholder':"00.00mmol/L"}),)

    fbc_red_blood_cell = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control",'oninput':"your_rbc()"}),)
    fbc_red_blood_range = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'id':"redbc",'disabled':"true", 'placeholder':"00.00 trillion/L"}),)
    fbc_hemoglobin = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control",'oninput':"your_hemoglobin()"}),)
    fbc_hemoglobin_range = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'id':"hemoglobin",'disabled':"true", 'placeholder':"00.00 g/dL"}),)
    fbc_hematocrit = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control",'oninput':"your_hematocrit()"}),)
    fbc_hematocrit_range = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'id':"hematocrit",'disabled':"true", 'placeholder':"00%"}),)
    fbc_white_blood_cell = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control",'oninput':"your_wbc()"}),)
    fbc_white_blood_range = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'id':"whitebc",'disabled':"true", 'placeholder':"00.00 billion/L"}),)
    fbc_platelet_count = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control",'oninput':"your_platelet()"}),)
    fbc_platelet_count_range = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'id':"platelet",'disabled':"true", 'placeholder':"00.00 billion/L"}),)
    fbc_neutrophil_count = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control",'oninput':"your_neutrophil()"}),)
    fbc_neutrophil_count_range = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'id':"neutrophil",'disabled':"true", 'placeholder':"00%"}),)
    fbc_lymphocyte_count = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control",'oninput':"your_lymphocyte()"}),)
    fbc_lymphocyte_count_range = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'id':"lymphocyte",'disabled':"true", 'placeholder':"00%"}),)
    full_blood_count_date = forms.DateField( required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                  input_formats=["%Y-%m-%d"])
    next_full_blood_count_date = forms.DateField(required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                  input_formats=["%Y-%m-%d"])
    docs_comments = forms.CharField(required=False, max_length=3000,widget=forms.Textarea(attrs={'class': "form-control md-textarea", 'rows': 3}), )
    fbc_image_scan = forms.ImageField()
    observation = forms.CharField(required=False, max_length=5000,widget=forms.Textarea(attrs={'class': "form-control md-textarea", 'rows': 3}), )
    conclusion = forms.CharField(required=False, max_length=5000,widget=forms.Textarea(attrs={'class': "form-control md-textarea", 'rows': 3}), )
    urine_test_date = forms.DateField( required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                  input_formats=["%Y-%m-%d"])
    next_urine_test = forms.DateField(required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                      input_formats=["%Y-%m-%d"])
    total_cholesterol = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_totalcholesterol()"}), )
    ldl_cholesterol = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_ldlcholesterol()"}), )
    hdl_cholesterol = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_hdlcholesterol()"}), )
    triglycerides = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_triglycerides()"}), )
    lipid_profile_date = forms.DateField( required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                  input_formats=["%Y-%m-%d"])
    next_lipid_test = forms.DateField( required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                  input_formats=["%Y-%m-%d"])
    docs_comments = forms.CharField(required=False, max_length=3000,widget=forms.Textarea(attrs={'class': "form-control md-textarea", 'rows': 3}), )
    lipid_scan = forms.ImageField()
    creatinine = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_creatinine()"}), )
    urea = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_urea()"}), )
    gfr = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_gfr()"}), )
    renal_test_date = forms.DateField(required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                      input_formats=["%Y-%m-%d"])
    next_renal_test = forms.DateField(required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                      input_formats=["%Y-%m-%d"])
    docs_comments = forms.CharField(required=False, max_length=3000,widget=forms.Textarea(attrs={'class': "form-control md-textarea", 'rows': 3}), )
    renal_scan = forms.ImageField()
    alt = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_alt()"}), )
    ast = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_ast()"}), )
    alp = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_alp()"}), )
    albumin = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_albumin()"}), )
    total_protein = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_totalprotein()"}), )
    bilirubin = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_bilirubin()"}), )
    bilirubin_direct = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_bilirubindirect()"}), )
    ggt = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_ggt()"}), )
    liver_test_date = forms.DateField(required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                      input_formats=["%Y-%m-%d"])
    next_liver_test = forms.DateField(required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                      input_formats=["%Y-%m-%d"])
    docs_comments = forms.CharField(required=False, max_length=3000,widget=forms.Textarea(attrs={'class': "form-control md-textarea", 'rows': 3}), )
    liver_scan = forms.ImageField()
    psa_total = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_psatotal()"}), )
    psa_test_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                    input_formats=["%Y-%m-%d"])
    next_psa_test = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                    input_formats=["%Y-%m-%d"])
    docs_comments = forms.CharField(required=False, max_length=3000,widget=forms.Textarea(attrs={'class': "form-control md-textarea", 'rows': 3}), )
    psa_scan = forms.ImageField()




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

class Addusersurgery(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), )
    doctor = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), )
    hospital = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), )
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                  input_formats=["%Y-%m-%d"])

class Adduserbmi(forms.Form):
    height = forms.CharField(max_length=255, widget=forms.NumberInput(attrs={'class': "form-control", 'oninput': "your_bmi()"}),)
    weight = forms.CharField(max_length=255, widget=forms.NumberInput(attrs={'class': "form-control", 'oninput': "your_bmi()"}),)

class Addbloodpressure(forms.Form):
    systolic = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control bpressure", "oninput": "your_bp()"}), )
    diastolic = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control bpressure", "oninput": "your_bp()"}), )

class Addcontactus(forms.Form):
    yourname = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}),)
    youremail = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), )
    yournumber = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), )
    subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': "form-control"}), )
    message = forms.CharField(max_length=1500, widget=forms.Textarea(attrs={'class': "form-control md-textarea textarea-style", "row":'5'}), )

class Addfastbloodsugar(forms.Form):
    fbs_test_result = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_fbs()"}), )
    fbs_test_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                    input_formats=["%Y-%m-%d"])
    next_fbs_test = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                    input_formats=["%Y-%m-%d"])
    fbs_saved_result = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'id': "fbs", 'disabled': "true", 'placeholder': "00.00mmol/L"}), )
    docs_comments = forms.CharField(required=False, max_length=3000,widget=forms.Textarea(attrs={'class': "form-control md-textarea", 'rows': 3}), )



class  Addfullbloodcount(forms.Form):
    red_blood_cell = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_rbc()"}), )
    fbc_red_blood_range = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'id': "redbc", 'disabled': "true", 'placeholder': "00.00 trillion/L"}), )
    hemoglobin = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_hemoglobin()"}), )
    fbc_hemoglobin_range = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'id': "hemoglobin", 'disabled': "true", 'placeholder': "00.00 g/dL"}), )
    hematocrit = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_hematocrit()"}), )
    fbc_hematocrit_range = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'id': "hematocrit", 'disabled': "true", 'placeholder': "00%"}), )
    white_blood_cell = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_wbc()"}), )
    fbc_white_blood_range = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'id': "whitebc", 'disabled': "true", 'placeholder': "00.00 billion/L"}), )
    platelet = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_platelet()"}), )
    fbc_platelet_count_range = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'id': "platelet", 'disabled': "true", 'placeholder': "00.00 billion/L"}), )
    neutrophil = forms.CharField(required=False, max_length=255, widget=forms.TextInput(
        attrs={'class': "form-control", 'oninput': "your_neutrophil()"}), )
    fbc_neutrophil_count_range = forms.CharField(required=False, max_length=255, widget=forms.TextInput(
        attrs={'class': "form-control", 'id': "neutrophil", 'disabled': "true", 'placeholder': "00%"}), )
    lymphocyte = forms.CharField(required=False, max_length=255, widget=forms.TextInput(
        attrs={'class': "form-control", 'oninput': "your_lymphocyte()"}), )
    fbc_lymphocyte_count_range = forms.CharField(required=False, max_length=255, widget=forms.TextInput(
        attrs={'class': "form-control", 'id': "lymphocyte", 'disabled': "true", 'placeholder': "00%"}), )
    full_blood_count_date = forms.DateField(required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),input_formats=["%Y-%m-%d"])
    next_full_blood_count_date = forms.DateField(required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),input_formats=["%Y-%m-%d"])
    fbc_image_scan = forms.ImageField()
    docs_comments = forms.CharField(required=False, max_length=3000,widget=forms.Textarea(attrs={'class': "form-control md-textarea", 'rows': 3}), )



class Adduserlipidprofile(forms.Form):
    total_cholesterol = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_totalcholesterol()"}), )
    ldl_cholesterol = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_ldlcholesterol()"}), )
    hdl_cholesterol = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_hdlcholesterol()"}), )
    triglycerides = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_triglycerides()"}), )
    lipid_profile_date = forms.DateField(required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                         input_formats=["%Y-%m-%d"])
    next_lipid_test = forms.DateField(required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                      input_formats=["%Y-%m-%d"])
    lipid_scan = forms.ImageField()
    docs_comments = forms.CharField(required=False, max_length=3000,widget=forms.Textarea(attrs={'class': "form-control md-textarea", 'rows': 3}), )


class Adduserrenaltest(forms.Form):
    creatinine = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_creatinine()"}), )
    urea = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_urea()"}), )
    gfr = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_gfr()"}), )
    renal_test_date = forms.DateField(required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                         input_formats=["%Y-%m-%d"])
    next_renal_test = forms.DateField(required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                         input_formats=["%Y-%m-%d"])
    renal_scan = forms.ImageField()
    docs_comments = forms.CharField(required=False, max_length=3000,widget=forms.Textarea(attrs={'class': "form-control md-textarea", 'rows': 3}), )


class Adduserlivertest(forms.Form):
    alt = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_alt()"}), )
    ast = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_ast()"}), )
    alp = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_alp()"}), )
    total_protein = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_totalprotein()"}), )
    bilirubin = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_bilirubin()"}), )
    bilirubin_direct = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_bilirubindirect()"}), )
    ggt = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_ggt()"}), )
    liver_test_date = forms.DateField(required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                         input_formats=["%Y-%m-%d"])
    next_liver_test = forms.DateField(required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                         input_formats=["%Y-%m-%d"])
    liver_scan = forms.ImageField()
    docs_comments = forms.CharField(required=False, max_length=3000,widget=forms.Textarea(attrs={'class': "form-control md-textarea", 'rows': 3}), )


class Adduserurinetest(forms.Form):
    observation = forms.CharField(required=False, max_length=5000,widget=forms.Textarea(attrs={'class': "form-control md-textarea", 'rows': 3}), )
    conclusion = forms.CharField(required=False, max_length=5000,widget=forms.Textarea(attrs={'class': "form-control md-textarea", 'rows': 3}), )
    urine_test_date = forms.DateField(required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                      input_formats=["%Y-%m-%d"])
    next_urine_test = forms.DateField(required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                      input_formats=["%Y-%m-%d"])


class Addprostatetest(forms.Form):
    psa_total = forms.CharField(required=False, max_length=255,widget=forms.TextInput(attrs={'class': "form-control", 'oninput': "your_psatotal()"}), )
    docs_comments = forms.CharField(required=False, max_length=3000,widget=forms.Textarea(attrs={'class': "form-control md-textarea", 'rows': 3}), )
    psa_test_date = forms.DateField(required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                         input_formats=["%Y-%m-%d"])
    next_psa_test = forms.DateField(required=False,widget=forms.DateInput(attrs={'class': 'datepicker form-control'}),
                                         input_formats=["%Y-%m-%d"])
    psa_scan = forms.ImageField()



