import datetime
from core.core_util import add_zeros
from core.forms.core_forms import NewUserForm,NewUserMedicalHistoryForm
from core.models import AuthUserDemographic
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

# Create your views here.
import random


def dashboard(request):
    return render(request,'dashboard.html')

def add_new_user(request):
    print ("1")
    if request.method == "POST":
        new_user_form = NewUserForm(request.POST, request.FILES)
        print ("2")
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

                                                )
                user_info.save()

                user_info.unique_id = '{}{}{}{}'.format(now.day,now.month,
                                                        now.year,add_zeros(5,str(user_info.id)))

                user_info.save()

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


            height = new_medical.cleaned_data['height']
            weight = new_medical.cleaned_data['weight']
            bp = new_medical.cleaned_data['bp']
            diabetes_mellitus = new_medical.cleaned_data['diabetes_mellitus']
            systematic_hypertension = new_medical.cleaned_data['systematic_hypertension']
            epilepsy = new_medical.cleaned_data['epilepsy']
            uterine_fibroid = new_medical.cleaned_data['uterine_fibroid']
            peptic_ulcer_disease = new_medical.cleaned_data['peptic_ulcer_disease']

            other_condition = new_medical.cleaned_data.get('other_condition')
            print(other_condition)
            medicine = new_medical.cleaned_data['medicine']
            dosage = new_medical.cleaned_data['dosage']
            refill_date = new_medical.cleaned_data['refill_date']

            allergy_name = new_medical.cleaned_data['allergy_name']
            allergy_type = new_medical.cleaned_data['allergy_type']
            alcohol = new_medical.cleaned_data['alcohol']
            smoking = new_medical.cleaned_data['smoking']
            surgery_date = new_medical.cleaned_data['surgery_date']
            surgery_name = new_medical.cleaned_data['surgery_name']


        else:
            messages.error(request,"Something went wrong")
            context = {'new_medical': new_medical, 'user': user}
            return render(request, 'medical-info.html', context)

    new_medical = NewUserMedicalHistoryForm()
    context = {'new_medical': new_medical,'user':user}
    return render(request,'medical-info.html',context)

