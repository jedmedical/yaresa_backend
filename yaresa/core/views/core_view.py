import datetime
from core.core_util import add_zeros
from core.forms.core_forms import NewUserForm, NewUserMedicalHistoryForm, Addusercondition, Adduserallergy, \
    Addusermedication
from core.models import AuthUserDemographic, Med_graphic, Height, Weight, Blood_Pressure, Medical_history, Medication, \
    Allergy, Social_history, Surgery
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
import requests


# Create your views here.
import random


def dashboard(request):

    return render(request,'dashboard.html')

def add_new_user(request):

    if request.method == "POST":
        new_user_form = NewUserForm(request.POST, request.FILES)

        if new_user_form.is_valid():
            picture = new_user_form.cleaned_data['picture']
            title = new_user_form.cleaned_data['title']
            first_name = new_user_form.cleaned_data['first_name']
            other_name = new_user_form.cleaned_data['other_name']

            surname = new_user_form.cleaned_data['surname']
            sex = new_user_form.cleaned_data['sex']

            date_of_birth = new_user_form.cleaned_data['date_of_birth']

            nationality = new_user_form.cleaned_data['nationality']
            religion = new_user_form.cleaned_data['religion']
            marital_status = new_user_form.cleaned_data['marital_status']
            address = new_user_form.cleaned_data['address']
            occupation = new_user_form.cleaned_data['occupation']
            email = new_user_form.cleaned_data['email']
            mobile = new_user_form.cleaned_data['mobile']
            emergency_contact_name = new_user_form.cleaned_data['emergency_contact_name']
            emergency_contact_mobile = new_user_form.cleaned_data['emergency_contact_mobile']
            # blood_group = new_user_form.cleaned_data['blood_group']
            # sickling_status = new_user_form.cleaned_data['sickling_status']
            # g6pd = new_user_form.cleaned_data['g6pd']

            pin = random.randint(1000,9999)
            unique_id="1"
            print("3")
            now = datetime.datetime.now()

            try:
                user = User.objects.create_user(username=mobile, password=pin,
                                               )

                user_info = AuthUserDemographic(user=user,email=email,picture=picture,
                                                title=title,first_name=first_name,other_name=other_name,
                                                surname=surname,sex=sex,date_of_birth=date_of_birth,
                                                nationality=nationality,religion=religion,
                                                marital_status=marital_status,address=address,
                                                occupation=occupation,emergency_contact_name=emergency_contact_name,
                                                emergency_contact_mobile=emergency_contact_mobile,
                                                mobile=mobile

                                                )


                user_info.save()

                user_info.unique_id = '{}{}{}{}'.format(now.day,now.month,
                                                        now.year,add_zeros(5,str(user_info.id)))

                user_info.save()

                sendsms(request,mobile,pin)



                return redirect("add-medi-info/{}".format(user_info.id))
            except IntegrityError as e:
                # if 'unique constraint' in e.args[0]:
                    messages.error(request, 'User already exist')





        context = {'new_user_form':new_user_form}
        return render(request,'add_new_user.html',context)

    new_user_form = NewUserForm()
    context = {'new_user_form':new_user_form}
    return render(request,'add_new_user.html',context)


def add_medical_info(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)
    if request.method == "POST":
        new_medical = NewUserMedicalHistoryForm(request.POST)

        if new_medical.is_valid():
            blood_group = new_medical.cleaned_data['blood_group']
            sickling_status = new_medical.cleaned_data['sickling_status']
            g6pd = new_medical.cleaned_data['g6pd']
            medi_graph = Med_graphic(user=user,blood_group=blood_group,
                                     sickling_status=sickling_status,
                                     g6pd=g6pd)
            medi_graph.save()

            height = new_medical.cleaned_data['height']
            weight = new_medical.cleaned_data['weight']
            bp = new_medical.cleaned_data['bp']

            Height(height=height).save()
            Weight(weight=weight).save()
            Blood_Pressure(bp=bp).save()

            diabetes_mellitus = new_medical.cleaned_data['diabetes_mellitus']
            if diabetes_mellitus == 'yes':
                Medical_history(user=user,condition="Diabetes Mellitus").save()
            systematic_hypertension = new_medical.cleaned_data['systematic_hypertension']
            if systematic_hypertension == 'yes':
                Medical_history(user=user,condition="Systematic Hypertension").save()
            epilepsy = new_medical.cleaned_data['epilepsy']
            if epilepsy == 'yes':
                Medical_history(user=user,condition="Ellipsis").save()
            uterine_fibroid = new_medical.cleaned_data['uterine_fibroid']
            if uterine_fibroid == 'yes':
                Medical_history(user=user,condition="Uterine Fibroid").save()
            peptic_ulcer_disease = new_medical.cleaned_data['peptic_ulcer_disease']
            if peptic_ulcer_disease == 'yes':
                Medical_history(user=user,condition="Peptic Ulcer Disease").save()

            other_condition = new_medical.cleaned_data.get('other_condition')
            if other_condition:
                Medical_history(user=user,condition=other_condition).save()
            print(other_condition)
            medicine = new_medical.cleaned_data['medicine']
            dosage = new_medical.cleaned_data['dosage']
            refill_date = new_medical.cleaned_data['refill_date']
            if medicine:
                Medication(user=user,medicine=medicine,dosage=dosage,refill_date=refill_date).save()

            allergy_name = new_medical.cleaned_data['allergy_name']
            allergy_type = new_medical.cleaned_data['allergy_type']

            if allergy_name:
                Allergy(user=user,name=allergy_name,type=allergy_type).save()

            alcohol = new_medical.cleaned_data['alcohol']
            social_history = Social_history(user=user)
            if alcohol == 'yes':
                social_history.alcohol=True

            smoking = new_medical.cleaned_data['smoking']
            if smoking == 'yes':
                social_history.smoking=True
            social_history.save()
            surgery_date = new_medical.cleaned_data['surgery_date']
            surgery_name = new_medical.cleaned_data['surgery_name']
            Surgery(user=user,name=surgery_name,date=surgery_date).save()
            messages.error(request, "Medical Info added")
            redirect('user-list')

        else:
            messages.error(request,"Please fill form completely")
            context = {'new_medical': new_medical, 'user': user}
            return render(request, 'medical-info.html', context)

    new_medical = NewUserMedicalHistoryForm()
    context = {'new_medical': new_medical,'user':user}
    return render(request,'medical-info.html',context)

def user_list(request):
    user = AuthUserDemographic.objects.all()

    context = {'user_list':user}
    return render(request, 'user_list.html', context)

def user_detail(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    context = {'user': user}
    return render(request, 'user_detail.html', context)


def user_condition(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    if request.method == "POST":
        userconditionform = Addusercondition(request.POST)
        if userconditionform.is_valid():
            Medical_history(user=user,condition=userconditionform.cleaned_data['condition']).save()
            messages.success(request,"Condition Added")


    userconditionform = Addusercondition()

    conditions = Medical_history.objects.filter(user=user)
    context = {'conditions': conditions,'user':user, 'userconditionform':userconditionform}
    return render(request, 'user-condition.html', context)


def user_allergy(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    if request.method == "POST":
        userallergyform = Adduserallergy(request.POST)
        if userallergyform.is_valid():
            Allergy(user=user,name=userallergyform.cleaned_data['allergy_name'],
                    type=userallergyform.cleaned_data['allergy_type']).save()
            messages.success(request,"Allergy Added")


    userallergyform = Adduserallergy()

    allergies = Allergy.objects.filter(user=user)
    context = {'allergies': allergies,'user':user, 'userallergyform':userallergyform}
    return render(request, 'user-allergy.html', context)

def user_medication(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    if request.method == "POST":
        usermedicationform = Addusermedication(request.POST)
        if usermedicationform.is_valid():
            Medication(user=user,medicine=usermedicationform.cleaned_data['medicine'],
                    dosage=usermedicationform.cleaned_data['dosage'],refill_date=usermedicationform.cleaned_data['refill_date']).save()
            messages.success(request,"Medicine Added")


    usermedicationform = Addusermedication()

    medications = Medication.objects.filter(user=user)
    context = {'medications': medications,'user':user, 'usermedicationform':usermedicationform}
    return render(request, 'user-medication.html', context)




def sendsms(request,contact,pin):
    url = "http://sms.nasaramobile.com/api/v2/sendsms"

    querystring = {"api_key": "5bc2dfb823e475bc2dfb823e88", "phone_numbers": "0548867947",
                   "sender_id": "Yaresa", "message": "Thanks for registering for Yaresa services. Download Yaresa app at .Your temporal pin is "}



    response = requests.get( url="http://sms.nasaramobile.com/api?"
                                    "api_key=5bc2dfb823e475bc2dfb823e88&&sender_id=Yaresa"
                                    "&&phone="+str(contact)+"&&message=Thanks for registering for Yaresa services. "
                                 "Download Yaresa app at .Your temporal pin is "+str(pin))
    print(response)
    print(response.reason)
    print(response.content)
