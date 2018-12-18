import datetime

from django.db.models import Count

from core.core_util import add_zeros
from core.forms.core_forms import NewUserForm, NewUserMedicalHistoryForm, Addusercondition, Adduserallergy, \
    Addusermedication, Adduserbmi, Addbloodpressure, Addcontactus, Addusersurgery, Addfastbloodsugar, \
    Addfullbloodcount, Adduserlipidprofile
from core.models import AuthUserDemographic, Med_graphic, Height, Weight, Blood_Pressure, Medical_history, Medication, \
    Allergy, Social_history, Surgery, Contactus, Fasting_blood_sugar, Full_blood_count, Lipid_profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404, Http404
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

            try:

                    blood_group = new_medical.cleaned_data['blood_group']
                    sickling_status = new_medical.cleaned_data['sickling_status']
                    g6pd = new_medical.cleaned_data['g6pd']
                    medi_graph = Med_graphic(user=user,blood_group=blood_group,
                                             sickling_status=sickling_status,
                                             g6pd_status=g6pd)
                    medi_graph.save()

                    height = new_medical.cleaned_data['height']
                    weight = new_medical.cleaned_data['weight']
                    systolic = new_medical.cleaned_data['systolic']
                    diastolic = new_medical.cleaned_data['diastolic']

                    Height(user=user,height=height).save()
                    Weight(user=user,weight=weight).save()
                    Blood_Pressure(user=user,systolic=systolic,diastolic=diastolic).save()

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
                    if new_medical.cleaned_data.get('other_condition_1'):
                        Medical_history(user=user, condition=new_medical.cleaned_data.get('other_condition_1')).save()
                    if new_medical.cleaned_data.get('other_condition_2'):
                        Medical_history(user=user, condition=new_medical.cleaned_data.get('other_condition_2')).save()
                    if new_medical.cleaned_data.get('other_condition_3'):
                            Medical_history(user=user, condition=new_medical.cleaned_data.get('other_condition_3')).save()

                    medicine = new_medical.cleaned_data['medicine']
                    dosage = new_medical.cleaned_data['dosage']
                    refill_date = new_medical.cleaned_data['refill_date']
                    if medicine and refill_date:
                        Medication(user=user,medicine=medicine,dosage=dosage,refill_date=refill_date).save()


                    medicine1 = new_medical.cleaned_data.get('medicine_1')
                    dosage1 = new_medical.cleaned_data.get('dosage_1')
                    refill_date1 = new_medical.cleaned_data.get('refill_date_1')
                    if medicine1 and refill_date1:
                        Medication(user=user,medicine=medicine1,dosage=dosage1,refill_date=refill_date1).save()

                    allergy_name = new_medical.cleaned_data['allergy_name']
                    allergy_type = new_medical.cleaned_data['allergy_type']

                    if allergy_name and allergy_type:
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
                    surgery_doctor = new_medical.cleaned_data['surgery_doctor']
                    surgery_hospital = new_medical.cleaned_data['surgery_hospital']
                    if surgery_name and surgery_date:
                        Surgery(user=user,name=surgery_name,date=surgery_date,doctor=surgery_doctor,hospital=surgery_hospital).save()

                    surgery_date1 = new_medical.cleaned_data.get('surgery_date_1')
                    surgery_name1 = new_medical.cleaned_data.get('surgery_name_1')
                    surgery_doctor1 = new_medical.cleaned_data.get('surgery_doctor_1')
                    surgery_hospital1 = new_medical.cleaned_data.get('surgery_hospital_1')

                    if surgery_name1 and surgery_date1:
                        Surgery(user=user, name=surgery_name1, date=surgery_date1,doctor=surgery_doctor1,hospital=surgery_hospital1).save()

                    fbs_test_result = new_medical.cleaned_data['fbs_test_result']
                    fbs_test_date = new_medical.cleaned_data['fbs_test_date']
                    fbs_saved_result = new_medical.cleaned_data['fbs_saved_result']

                    if fbs_test_result and fbs_test_date:
                        Fasting_blood_sugar(user=user, test_result=fbs_test_result, test_date=fbs_test_date, saved_result=fbs_saved_result).save()

                    fbc_red_blood_cell = new_medical.cleaned_data['fbc_red_blood_cell']
                    fbc_red_blood_range = new_medical.cleaned_data.get('fbc_red_blood_range')
                    fbc_hemoglobin = new_medical.cleaned_data['fbc_hemoglobin']
                    fbc_hemoglobin_range = new_medical.cleaned_data['fbc_hemoglobin_range']
                    fbc_hematocrit = new_medical.cleaned_data['fbc_hematocrit']
                    fbc_hematocrit_range = new_medical.cleaned_data['fbc_hematocrit_range']
                    fbc_white_blood_cell = new_medical.cleaned_data['fbc_white_blood_cell']
                    fbc_white_blood_range = new_medical.cleaned_data['fbc_white_blood_range']
                    fbc_platelet_count = new_medical.cleaned_data['fbc_platelet_count']
                    fbc_platelet_count_range = new_medical.cleaned_data['fbc_platelet_count_range']
                    full_blood_count_date = new_medical.cleaned_data['full_blood_count_date']
                    next_full_blood_count_date = new_medical.cleaned_data['next_full_blood_count_date']
                    fbc_image_scan = new_medical.cleaned_data['fbc_image_scan']
                    fbc_neutrophil_count = new_medical.cleaned_data['fbc_neutrophil_count']
                    fbc_lymphocyte_count = new_medical.cleaned_data['fbc_lymphocyte_count']

                    if fbc_red_blood_cell and fbc_hemoglobin:
                        Full_blood_count(user=user, red_blood_cell=fbc_red_blood_cell, hemoglobin=fbc_hemoglobin,hematocrit=fbc_hematocrit,
                                         white_blood_cell=fbc_white_blood_cell,platelet=fbc_platelet_count,date=full_blood_count_date,
                                         red_blood_range=fbc_red_blood_range,hemoglobin_range=fbc_hemoglobin_range,hematocrit_range=fbc_hematocrit_range,
                                         white_blood_range=fbc_white_blood_range,platelet_range=fbc_platelet_count_range,next_test_date=next_full_blood_count_date,
                                         test_scan=fbc_image_scan,neutrophil=fbc_neutrophil_count,lymphocyte=fbc_lymphocyte_count).save()

                    total_cholesterol = new_medical.cleaned_data['total_cholesterol']
                    hdl_cholesterol = new_medical.cleaned_data['hdl_cholesterol']
                    ldl_cholesterol = new_medical.cleaned_data['ldl_cholesterol']
                    triglycerides = new_medical.cleaned_data['triglycerides']
                    lipid_profile_date = new_medical.cleaned_data['lipid_profile_date']
                    next_lipid_test = new_medical.cleaned_data['next_lipid_test']
                    lipid_scan = new_medical.cleaned_data['lipid_scan']

                    if total_cholesterol and triglycerides:
                        Lipid_profile(user=user, total_cholesterol=total_cholesterol, hdl_cholesterol=hdl_cholesterol, ldl_cholesterol=ldl_cholesterol,
                                      triglycerides=triglycerides,date=lipid_profile_date,next_lipid_test=next_lipid_test,lipid_scan=lipid_scan).save()

                    messages.success(request, "Medical Info added")
            except:
                messages.error(request, "Something went wrong")

            return redirect('core:user-list')
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

def user_bmi(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    if request.method == "POST":
        userbmiform = Adduserbmi(request.POST)
        if userbmiform.is_valid():
            Height(user=user,height=userbmiform.cleaned_data['height']).save()
            Weight(user=user,weight=userbmiform.cleaned_data['weight']).save()
            messages.success(request, "BMI Added")


    userbmiform = Adduserbmi()

    heights = Height.objects.filter(user=user)
    weights = Weight.objects.filter(user=user)
    context = {'height': heights, 'weight': weights, 'user': user, 'userbmiform': userbmiform}
    return render(request, 'user-bmi.html', context)

def user_bloodpressure(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    if request.method == "POST":
        userbpressureform = Addbloodpressure(request.POST)
        if userbpressureform.is_valid():
            Blood_Pressure(user=user, systolic=userbpressureform.cleaned_data['systolic'], diastolic=userbpressureform.cleaned_data['diastolic']).save()
            messages.success(request, "Blood Pressure Added")

    userbpressureform = Addbloodpressure()

    bpressure = Blood_Pressure.objects.filter(user=user)
    context = {'bpressure': bpressure, 'user': user, 'userbpressureform': userbpressureform}
    return render(request, 'user-bloodpressure.html', context)


def user_surgery(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    if request.method == "POST":
        usersurgeryform = Addusersurgery(request.POST)
        if usersurgeryform.is_valid():
            Surgery(user=user, name=usersurgeryform.cleaned_data['name'], date=usersurgeryform.cleaned_data['date'], doctor=usersurgeryform.cleaned_data['doctor'], hospital=usersurgeryform.cleaned_data['hospital']).save()
            messages.success(request, "Surgery Added")

    usersurgeryform = Addusersurgery()

    surgerydone = Surgery.objects.filter(user=user)
    context = {'surgerydone':surgerydone, 'user':user, 'usersurgeryform':usersurgeryform}
    return render(request, 'user-surgery.html', context)



def user_account_reset(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)
    user.first_login=True
    patient = user.user
    pin = random.randint(1000, 9999)
    patient.set_password(pin)
    sendsms(request,patient.username,pin)
    user.save()
    messages.success(request,"Medicine Added")

    return




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


def blood_group_count(request):
    fieldname = 'blood_group'
    blood_group_count = Med_graphic.objects.values(fieldname).order_by(fieldname).annotate(the_count=Count(fieldname))

    Aplus =0
    bplus =0
    abplus =0
    oplus = 0
    Aneg = 0
    bneg = 0
    abneg = 0
    oneg = 0

    for i in blood_group_count:
        print (i['blood_group'])
        if i['blood_group'] == "A+":
            Aplus = i['the_count']
        if i['blood_group'] == "B+":
            bplus = i['the_count']
        if i['blood_group'] == "AB+":
            abplus = i['the_count']

        if i['blood_group'] == "O+":
            oplus = i['the_count']
        if i['blood_group'] == "A-":
            Aneg = i['the_count']
        if i['blood_group'] == "B-":
            bneg = i['the_count']
        if i['blood_group'] == "AB-":
            abneg = i['the_count']
        if i['blood_group'] == "O-":
            oneg = i['the_count']

    context = {"aplus":Aplus,"aneg":Aneg,"bplus":bplus,
               "bneg":bneg,"abplus":abplus,"abneg":abneg,
               "oplus":oplus,"oneg":oneg}
    return render(request, 'blood-group-count.html', context)

def sickling_count(request):
    fieldname = 'sickling_status'
    sickling_status_count = Med_graphic.objects.values(fieldname).order_by(fieldname).annotate(the_count=Count(fieldname))

    aa =0
    ass =0
    ss =0
    sc = 0

    for i in sickling_status_count:
        print (i['sickling_status'])
        if i['sickling_status'] == "AA":
            aa = i['the_count']
        if i['sickling_status'] == "AS":
            ass = i['the_count']
        if i['sickling_status'] == "SS":
            ss = i['the_count']

        if i['sickling_status'] == "SC":
            sc = i['the_count']

    context = {"aa":aa,"ass":ass,"ss":ss,
               "sc":sc,}
    return render(request, 'sickling-status-count.html', context)

def g6pd_count(request):
    fieldname = 'g6pd_status'
    g6pd_count = Med_graphic.objects.values(fieldname).order_by(fieldname).annotate(the_count=Count(fieldname))

    normal = 0
    partial_defect = 0
    full_defect = 0

    for i in g6pd_count:
        print(i['g6pd'])
        if i['g6pd'] == "NORMAL":
            normal = i['the_count']
        if i['g6pd'] == "PARTIAL DEFECT":
            partial_defect = i['the_count']
        if i['g6pd'] == "FULL DEFECT":
            full_defect = i['the_count']

    context = {"normal":normal, "partial_defect":partial_defect, "full_defect":full_defect}
    return render(request, 'g6pd-count.html', context)

def contact_us(request,id):
    if request.method == "POST":
        visitorcontactform = Addcontactus(request.POST)
        if visitorcontactform.is_valid():
           Contactus(yourname=visitorcontactform.cleaned_data['yourname'],
            yournumber=visitorcontactform.cleaned_data['yournumber'],
            youremail=visitorcontactform.cleaned_data['youremail'],
            subject=visitorcontactform.cleaned_data['subject'],
            message=visitorcontactform.cleaned_data['message']).save()
        messages.success(request, "Message Sent")

    visitorcontactform = Addcontactus()
    contactusnow = Contactus.objects.filter(id=id)
    context = {'contactusnow':contactusnow, 'visitorcontactform':visitorcontactform}

    return render(request, "index.html", context)

def user_fastbloodsugar(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    if request.method == "POST":
        userfastbloodsugar = Addfastbloodsugar(request.POST)
        if userfastbloodsugar.is_valid():
            Fasting_blood_sugar(user=user, test_result=userfastbloodsugar.cleaned_data['fbs_test_result'],
                                test_date=userfastbloodsugar.cleaned_data['fbs_test_date'], saved_result=userfastbloodsugar.cleaned_data['fbs_saved_result']).save()
            messages.success(request, "Fasting Blood Sugar Added")

    userfastbloodsugar = Addfastbloodsugar()

    fastingbs = Fasting_blood_sugar.objects.filter(user=user)
    context = {'fastingbs':fastingbs, 'user':user, 'userfastbloodsugar':userfastbloodsugar}
    return render(request, 'user_fasting_blood_sugar.html', context)


def user_fullbloodcount(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    if request.method == "POST":
        userfullbloodcount = Addfullbloodcount(request.POST)
        if userfullbloodcount.is_valid():
            Full_blood_count(user=user, red_blood_cell=userfullbloodcount.cleaned_data['fbc_red_blood_cell'], hemoglobin=userfullbloodcount.cleaned_data['fbc_hemoglobin'],
                             hematocrit=userfullbloodcount.cleaned_data['fbc_hematocrit'],white_blood_cell=userfullbloodcount.cleaned_data['fbc_white_blood_cell'],
                             platelet=userfullbloodcount.cleaned_data['fbc_platelet_count'],date=userfullbloodcount.cleaned_data['full_blood_count_date'],
                             next_test_date=userfullbloodcount.cleaned_data['next_full_blood_count_date'],test_scan=userfullbloodcount.cleaned_data['fbc_image_scan'],
                             neutrophil=userfullbloodcount.cleaned_data['fbc_neutrophil_count'],lymphocyte=userfullbloodcount.cleaned_data['fbc_lymphocyte_count']).save()

            messages.success(request, "Full Blood Count Added")

    userfullbloodcount = Addfullbloodcount()

    fullcounts = Full_blood_count.objects.filter(user=user)
    context = {'fullcounts':fullcounts, 'user':user, 'userfullbloodcount':userfullbloodcount}
    return render(request, 'user-full-blood-count.html', context)


def user_lipidprofile(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    if request.method == "POST":
        userlipidprofile = Adduserlipidprofile(request.POST)
        if userlipidprofile.is_valid():
            Lipid_profile(user=user, total_cholesterol=userlipidprofile.cleaned_data['total_cholesterol'],hdl_cholesterol=userlipidprofile.cleaned_data['hdl_cholesterol'],
                          ldl_cholesterol=userlipidprofile.cleaned_data['ldl_cholesterol'],triglycerides=userlipidprofile.cleaned_data['triglycerides'],
                          date=userlipidprofile.cleaned_data['lipid_profile_date'],next_lipid_test=userlipidprofile.cleaned_data['next_lipid_test'],
                          lipid_scan=userlipidprofile.cleaned_data['lipid_scan']).save()

            messages.success(request, "Lipid Profile Added")

    userlipidprofile = Adduserlipidprofile()

    lipidprofile = Lipid_profile.objects.filter(user=user)
    context = {'lipidprofile':lipidprofile, 'user':user, 'userlipidprofile':userlipidprofile}
    return render(request, 'user-lipid-profile.html', context)















