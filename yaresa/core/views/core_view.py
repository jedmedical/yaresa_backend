import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Count

from core.core_util import add_zeros
from core.forms.core_forms import NewUserForm, NewUserMedicalHistoryForm, Addusercondition, Adduserallergy, \
    Addusermedication, Adduserbmi, Addbloodpressure, Addcontactus, Addusersurgery, Addfastbloodsugar, \
    Addfullbloodcount, Adduserlipidprofile, Adduserrenaltest, Adduserlivertest, Addprostatetest, Adduserurinetest, \
    Addorganization, PatientTransferForm, NewPartnerForm, Adddrugform
from core.fusioncharts import FusionCharts
from core.models import AuthUserDemographic, Med_graphic, Height, Weight, Blood_Pressure, Medical_history, Medication, \
    Allergy, Social_history, Surgery, Contactus, Fasting_blood_sugar, Full_blood_count, Lipid_profile, \
    Renal_function_test, Liver_function_test, Prostate_specific_antigen, Urine_test, Organization, Partners, \
    PatientPartnerTransfer, Drugs
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404, Http404
import requests


# Create your views here.
import random

@login_required(login_url='accounts/signin')
def dashboard(request):

    return render(request,'dashboard.html')

@login_required(login_url='accounts/signin')
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

                user.groups.add(Group.objects.get_or_create(name="Patient")[0])

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

@login_required(login_url='accounts/signin')
def add_medical_info(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)
    if request.method == "POST":
        new_medical = NewUserMedicalHistoryForm(request.POST, request.FILES)

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

                    drug = new_medical.cleaned_data['medicine']
                    medicine = Drugs.objects.get(id=drug)
                    dosage = new_medical.cleaned_data['dosage']
                    strength = new_medical.cleaned_data['strength']
                    refill_date = new_medical.cleaned_data['refill_date']
                    if medicine and refill_date:
                        Medication(user=user,medicine=medicine,dosage=dosage,strength=strength,refill_date=refill_date).save()

                    drug = new_medical.cleaned_data.get('medicine_1')
                    medicine1 = Drugs.objects.get(id=drug)
                    dosage1 = new_medical.cleaned_data.get('dosage_1')
                    strength1 = new_medical.cleaned_data.get('strength_1')
                    refill_date1 = new_medical.cleaned_data.get('refill_date_1')
                    if medicine1 and refill_date1:
                        Medication(user=user,medicine=medicine1,dosage=dosage1,strength=strength1,refill_date=refill_date1).save()

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
                    docs_comments = new_medical.cleaned_data['docs_comments']
                    if surgery_name and surgery_date:
                        Surgery(user=user,name=surgery_name,date=surgery_date,doctor=surgery_doctor,hospital=surgery_hospital
                                ,docs_comments=docs_comments).save()

                    surgery_date1 = new_medical.cleaned_data.get('surgery_date_1')
                    surgery_name1 = new_medical.cleaned_data.get('surgery_name_1')
                    surgery_doctor1 = new_medical.cleaned_data.get('surgery_doctor_1')
                    surgery_hospital1 = new_medical.cleaned_data.get('surgery_hospital_1')

                    if surgery_name1 and surgery_date1:
                        Surgery(user=user, name=surgery_name1, date=surgery_date1,doctor=surgery_doctor1,hospital=surgery_hospital1).save()

                    # fbs_test_result = new_medical.cleaned_data['fbs_test_result']
                    # fbs_test_date = new_medical.cleaned_data['fbs_test_date']
                    # fbs_saved_result = new_medical.cleaned_data['fbs_saved_result']
                    # next_fbs_test = new_medical.cleaned_data['next_fbs_test']
                    # docs_comments = new_medical.cleaned_data['docs_comments']
                    #
                    # if fbs_test_result and fbs_test_date:
                    #     Fasting_blood_sugar(user=user, test_result=fbs_test_result, test_date=fbs_test_date, saved_result=fbs_saved_result,docs_comments=docs_comments,
                    #                         next_fbs_test=next_fbs_test).save()
                    #
                    # red_blood_cell = new_medical.cleaned_data['fbc_red_blood_cell']
                    # fbc_red_blood_range = new_medical.cleaned_data.get('fbc_red_blood_range')
                    # hemoglobin = new_medical.cleaned_data['fbc_hemoglobin']
                    # fbc_hemoglobin_range = new_medical.cleaned_data['fbc_hemoglobin_range']
                    # hematocrit = new_medical.cleaned_data['fbc_hematocrit']
                    # fbc_hematocrit_range = new_medical.cleaned_data['fbc_hematocrit_range']
                    # white_blood_cell = new_medical.cleaned_data['fbc_white_blood_cell']
                    # fbc_white_blood_range = new_medical.cleaned_data['fbc_white_blood_range']
                    # platelet = new_medical.cleaned_data['fbc_platelet_count']
                    # fbc_platelet_count_range = new_medical.cleaned_data['fbc_platelet_count_range']
                    # full_blood_count_date = new_medical.cleaned_data['full_blood_count_date']
                    # next_full_blood_count_date = new_medical.cleaned_data['next_full_blood_count_date']
                    # fbc_image_scan = new_medical.cleaned_data['fbc_image_scan']
                    # neutrophil = new_medical.cleaned_data['fbc_neutrophil_count']
                    # lymphocyte = new_medical.cleaned_data['fbc_lymphocyte_count']
                    # docs_comments = new_medical.cleaned_data['docs_comments']
                    #
                    # if fbc_red_blood_cell and fbc_hemoglobin:
                    #     Full_blood_count(user=user, red_blood_cell=red_blood_cell, hemoglobin=hemoglobin,hematocrit=hematocrit,
                    #                      white_blood_cell=white_blood_cell,platelet=platelet,full_blood_count_date=full_blood_count_date,
                    #                      red_blood_range=fbc_red_blood_range,hemoglobin_range=fbc_hemoglobin_range,hematocrit_range=fbc_hematocrit_range,
                    #                      white_blood_range=fbc_white_blood_range,platelet_range=fbc_platelet_count_range,next_full_blood_count_date=next_full_blood_count_date,
                    #                      fbc_image_scan=fbc_image_scan,neutrophil=neutrophil,lymphocyte=lymphocyte,docs_comments=docs_comments).save()
                    #
                    # total_cholesterol = new_medical.cleaned_data['total_cholesterol']
                    # hdl_cholesterol = new_medical.cleaned_data['hdl_cholesterol']
                    # ldl_cholesterol = new_medical.cleaned_data['ldl_cholesterol']
                    # triglycerides = new_medical.cleaned_data['triglycerides']
                    # lipid_profile_date = new_medical.cleaned_data['lipid_profile_date']
                    # next_lipid_test = new_medical.cleaned_data['next_lipid_test']
                    # lipid_scan = new_medical.cleaned_data['lipid_scan']
                    # docs_comments = new_medical.cleaned_data['docs_comments']
                    #
                    # if total_cholesterol and triglycerides:
                    #     Lipid_profile(user=user, total_cholesterol=total_cholesterol, hdl_cholesterol=hdl_cholesterol, ldl_cholesterol=ldl_cholesterol,
                    #                   triglycerides=triglycerides,lipid_profile_date=lipid_profile_date,next_lipid_test=next_lipid_test,lipid_scan=lipid_scan,docs_comments=docs_comments).save()
                    #
                    # creatinine = new_medical.cleaned_data['creatinine']
                    # urea = new_medical.cleaned_data['urea']
                    # gfr = new_medical.cleaned_data['gfr']
                    # renal_test_date = new_medical.cleaned_data['renal_test_date']
                    # next_renal_test = new_medical.cleaned_data['next_renal_test']
                    # renal_scan = new_medical.cleaned_date['renal_scan']
                    # docs_comments = new_medical.cleaned_data['docs_comments']
                    #
                    # if creatinine and gfr:
                    #     Renal_function_test(user=user, creatinine=creatinine, urea=urea, renal_test_date=renal_test_date,
                    #                         next_renal_test=next_renal_test, renal_scan=renal_scan,docs_comments=docs_comments).save()
                    #
                    # alt = new_medical.cleaned_data['alt']
                    # ast = new_medical.cleaned_data['ast']
                    # alp = new_medical.cleaned_data['alp']
                    # total_protein = new_medical.cleaned_data['total_protein']
                    # bilirubin = new_medical.cleaned_data['bilirubin']
                    # bilirubin_direct = new_medical.cleaned_data['bilirubin_direct']
                    # ggt = new_medical.cleaned_data['ggt']
                    # liver_test_date = new_medical.cleaned_data['liver_test_date']
                    # next_liver_test = new_medical.cleaned_data['next_liver_test']
                    # liver_scan = new_medical.cleaned_data['liver_scan']
                    # docs_comments = new_medical.cleaned_data['docs_comments']
                    #
                    # if alt and ast:
                    #     Liver_function_test(user=user,alt=alt,ast=ast,alp=alp,total_protein=total_protein,bilirubin=bilirubin,bilirubin_direct=bilirubin_direct,
                    #                         ggt=ggt,liver_test_date=liver_test_date,next_liver_test=next_liver_test,liver_scan=liver_scan,docs_comments=docs_comments).save()
                    #
                    # psa_total = new_medical.cleaned_data['psa_total']
                    # psa_test_date = new_medical.cleaned_data['psa_test_date']
                    # next_psa_test = new_medical.cleaned_data['next_psa_test']
                    # docs_comments = new_medical.cleaned_data['docs_comments']
                    #
                    # if psa_total and psa_test_date:
                    #     Prostate_specific_antigen(user=user,psa_total=psa_total,psa_test_date=psa_test_date,next_psa_test=next_psa_test,docs_comments=docs_comments,psa_scan=psa_scan).save()
                    #
                    # observation = new_medical.cleaned_data['observation']
                    # conclusion = new_medical.cleaned_data['conclusion']
                    # urine_test_date = new_medical.cleaned_data['urine_test_date']
                    # next_urine_test = new_medical.cleaned_data['next_urine_test']
                    #
                    # if observation and conclusion:
                    #     Urine_test(user=user,observation=observation,conclusion=conclusion,urine_test_date=urine_test_date,
                    #                next_urine_test=next_urine_test).save()
                    #


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

@login_required(login_url='accounts/signin')
def user_list(request):
    user = AuthUserDemographic.objects.all()

    context = {'user_list':user}
    return render(request, 'user_list.html', context)

@login_required(login_url='accounts/signin')
def doctorpatients_list(request):
    user = AuthUserDemographic.objects.all()

    context = {'user_list':user}
    return render(request, 'doctor_patients_list.html', context)

@login_required(login_url='accounts/signin')
def user_detail(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    context = {'user': user}
    return render(request, 'user_detail.html', context)

@login_required(login_url='accounts/signin')
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

@login_required(login_url='accounts/signin')
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

@login_required(login_url='accounts/signin')
def user_medication(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    if request.method == "POST":
        usermedicationform = Addusermedication(request.POST)
        if usermedicationform.is_valid():
            dosage = usermedicationform.cleaned_data['dosage']
            strength = usermedicationform.cleaned_data['strength']
            refill_date = usermedicationform.cleaned_data['refill_date']
            drug = usermedicationform.cleaned_data['medicine']
            medicine = Drugs.objects.get(id=drug)

            if medicine and dosage:

                Medication(user=user, medicine=medicine, strength=strength,dosage=dosage, refill_date=refill_date).save()

                messages.success(request, "Medication Added")


    usermedicationform = Addusermedication()

    medications = Medication.objects.filter(user=user)
    context = {'medications': medications,'user':user, 'usermedicationform':usermedicationform}
    return render(request, 'user-medication.html', context)

@login_required(login_url='accounts/signin')
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

@login_required(login_url='accounts/signin')
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

@login_required(login_url='accounts/signin')
def user_surgery(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    if request.method == "POST":
        usersurgeryform = Addusersurgery(request.POST)
        if usersurgeryform.is_valid():
            Surgery(user=user, name=usersurgeryform.cleaned_data['name'], date=usersurgeryform.cleaned_data['date'],
                    doctor=usersurgeryform.cleaned_data['doctor'], hospital=usersurgeryform.cleaned_data['hospital'],
                    docs_comments=usersurgeryform.cleaned_data['docs_comments']).save()
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
    messages.success(request,"Password reset")

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

@login_required(login_url='accounts/signin')
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

    pie3d = FusionCharts("pie3d", "ex2", "100%", "400", "chart-1", "json",
                             # The data is passed as a string in the `dataSource` as parameter.
                             {
                                 "chart": {
                                     "caption": "Blood Group Chart",
                                     "subCaption" : "",
                                     "showValues":"1",
                                     "showPercentInTooltip" : "0",
                                     "numberPrefix" : "",
                                     "enableMultiSlicing":"1",
                                     "theme": "fusion"
                                 },
                                 "data": [{
                                     "label": "A+",
                                     "value": Aplus
                                 }, {
                                     "label": "A-",
                                     "value": Aneg
                                 }, {
                                     "label": "B+",
                                     "value": bplus
                                 }, {
                                     "label": "B-",
                                     "value": bneg
                                 }, {
                                     "label": "AB+",
                                     "value": abplus
                                 }, {
                                     "label": "AB-",
                                     "value": abneg
                                 }, {
                                     "label": "O+",
                                     "value": oplus
                                 }, {
                                     "label": "O-",
                                     "value": oneg
                                 }]
                             })

    context = {"aplus":Aplus,"aneg":Aneg,"bplus":bplus,
               "bneg":bneg,"abplus":abplus,"abneg":abneg,
               "oplus":oplus,"oneg":oneg,
               'outputchart' : pie3d.render(), }
    return render(request, 'blood-group-count.html', context)

@login_required(login_url='accounts/signin')
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

    pie3d = FusionCharts("pie3d", "ex2", "100%", "400", "chart-1", "json",
                         # The data is passed as a string in the `dataSource` as parameter.
                         {
                             "chart": {
                                 "caption": "Sickling Status Chart",
                                 "subCaption": "",
                                 "showValues": "1",
                                 "showPercentInTooltip": "0",
                                 "numberPrefix": "",
                                 "enableMultiSlicing": "1",
                                 "theme": "fusion"
                             },
                             "data": [{
                                 "label": "AA",
                                 "value": aa
                             }, {
                                "label": "AS",
                                "value": ass
                             }, {
                                 "label": "SS",
                                 "value": ss
                             }, {
                                 "label": "SC",
                                 "value": sc
                             }]
                         })

    context = {"aa":aa,"ass":ass,"ss":ss,
               "sc":sc,
               'outputchart':pie3d.render(),}
    return render(request, 'sickling-status-count.html', context)

@login_required(login_url='accounts/signin')
def g6pd_count(request):
    fieldname = 'g6pd_status'
    g6pd_count = Med_graphic.objects.values(fieldname).order_by(fieldname).annotate(the_count=Count(fieldname))

    print(g6pd_count)

    normal = 0
    partial_defect = 0
    full_defect = 0

    for i in g6pd_count:
        print(i['g6pd_status'])
        if i['g6pd_status'].upper() == "NORMAL":
            normal = i['the_count']
        if i['g6pd_status'].upper() == "PARTIAL DEFECT":
            partial_defect = i['the_count']
        if i['g6pd_status'].upper() == "FULL DEFECT":
            full_defect = i['the_count']

    pie3d = FusionCharts("pie3d", "ex2", "100%", "400", "chart-1", "json",
                         # The data is passed as a string in the `dataSource` as parameter.
                         {
                             "chart": {
                                 "caption": "G6PD Status Chart",
                                 "subCaption": "",
                                 "showValues": "1",
                                 "showPercentInTooltip": "0",
                                 "numberPrefix": "",
                                 "enableMultiSlicing": "1",
                                 "theme": "fusion"
                             },
                             "data": [{
                                 "label": "NORMAL",
                                 "value": normal
                             }, {
                                 "label": "PARTIAL DEFECT",
                                 "value": partial_defect
                             }, {
                                 "label": "FULL DEFECT",
                                 "value": full_defect
                             }]
                        })

    print(normal)
    context = {"normal":normal, "partial_defect":partial_defect, "full_defect":full_defect,
               'outputchart': pie3d.render(),}
    return render(request, 'g6pd-count.html', context)


def contact_us(request):
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
    contactusnow = Contactus.objects.filter(yourname=yourname)
    context = {'contactusnow':contactusnow, 'visitorcontactform':visitorcontactform}

    return render(request, "index.html", context)


@login_required(login_url='accounts/signin')
def user_fastbloodsugar(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    if request.method == "POST":
        userfastbloodsugar = Addfastbloodsugar(request.POST)
        if userfastbloodsugar.is_valid():
            Fasting_blood_sugar(user=user, test_result=userfastbloodsugar.cleaned_data['fbs_test_result'],
                                test_date=userfastbloodsugar.cleaned_data['fbs_test_date'], saved_result=userfastbloodsugar.cleaned_data['fbs_saved_result'],
                                next_fbs_test=userfastbloodsugar.cleaned_data['next_fbs_test'],docs_comments=userfastbloodsugar.cleaned_data['docs_comments']).save()
            messages.success(request, "Fasting Blood Sugar Added")

    userfastbloodsugar = Addfastbloodsugar()

    fastingbs = Fasting_blood_sugar.objects.filter(user=user)
    context = {'fastingbs':fastingbs, 'user':user, 'userfastbloodsugar':userfastbloodsugar}
    return render(request, 'user_fasting_blood_sugar.html', context)

@login_required(login_url='accounts/signin')
def user_fullbloodcount(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    if request.method == "POST":
        userfullbloodcount = Addfullbloodcount(request.POST,request.FILES)
        if userfullbloodcount.is_valid():
            Full_blood_count(user=user, red_blood_cell=userfullbloodcount.cleaned_data['red_blood_cell'], hemoglobin=userfullbloodcount.cleaned_data['hemoglobin'],
                             hematocrit=userfullbloodcount.cleaned_data['hematocrit'],white_blood_cell=userfullbloodcount.cleaned_data['white_blood_cell'],
                             platelet=userfullbloodcount.cleaned_data['platelet'],full_blood_count_date=userfullbloodcount.cleaned_data['full_blood_count_date'],
                             next_full_blood_count_date=userfullbloodcount.cleaned_data['next_full_blood_count_date'],fbc_image_scan=userfullbloodcount.cleaned_data['fbc_image_scan'],
                             neutrophil=userfullbloodcount.cleaned_data['neutrophil'],lymphocyte=userfullbloodcount.cleaned_data['lymphocyte'],
                             docs_comments=userfullbloodcount.cleaned_data['docs_comments']).save()

            messages.success(request, "Full Blood Count Added")
        else:
            fullcounts = Full_blood_count.objects.filter(user=user)
            context = {'fullcounts': fullcounts, 'user': user, 'userfullbloodcount': userfullbloodcount}
            return render(request, 'user-full-blood-count.html', context)

    userfullbloodcount = Addfullbloodcount()

    fullcounts = Full_blood_count.objects.filter(user=user)
    context = {'fullcounts':fullcounts, 'user':user, 'userfullbloodcount':userfullbloodcount}
    return render(request, 'user-full-blood-count.html', context)

@login_required(login_url='accounts/signin')
def user_lipidprofile(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    if request.method == "POST":
        userlipidprofile = Adduserlipidprofile(request.POST, request.FILES)
        if userlipidprofile.is_valid():
            Lipid_profile(user=user, total_cholesterol=userlipidprofile.cleaned_data['total_cholesterol'],hdl_cholesterol=userlipidprofile.cleaned_data['hdl_cholesterol'],
                          ldl_cholesterol=userlipidprofile.cleaned_data['ldl_cholesterol'],triglycerides=userlipidprofile.cleaned_data['triglycerides'],
                          lipid_profile_date=userlipidprofile.cleaned_data['lipid_profile_date'],next_lipid_test=userlipidprofile.cleaned_data['next_lipid_test'],
                          lipid_scan=userlipidprofile.cleaned_data['lipid_scan'],docs_comments=userlipidprofile.cleaned_data['docs_comments']).save()

            messages.success(request, "Lipid Profile Added")

    userlipidprofile = Adduserlipidprofile()

    lipidprofile = Lipid_profile.objects.filter(user=user)
    context = {'lipidprofile':lipidprofile, 'user':user, 'userlipidprofile':userlipidprofile}
    return render(request, 'user-lipid-profile.html', context)


@login_required(login_url='accounts/signin')
def user_renaltest(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    if request.method == "POST":
        userrenaltest = Adduserrenaltest(request.POST, request.FILES)
        if userrenaltest.is_valid():
            Renal_function_test(user=user, creatinine=userrenaltest.cleaned_data['creatinine'], urea=userrenaltest.cleaned_data['urea'],
                                gfr=userrenaltest.cleaned_data['gfr'], renal_test_date=userrenaltest.cleaned_data['renal_test_date'],
                                next_renal_test=userrenaltest.cleaned_data['next_renal_test'], renal_scan=userrenaltest.cleaned_date['renal_scan'],
                                docs_comments=userrenaltest.cleaned_data['docs_comments']).save()
            messages.success(request, "Renal Test Added")

    userrenaltest = Adduserrenaltest()

    renalfunction = Renal_function_test.objects.filter(user=user)
    context = {'renalfunction':renalfunction, 'user':user, 'userrenaltest':userrenaltest}
    return render(request, 'user-renal-function.html', context)


@login_required(login_url='accounts/signin')
def user_livertest(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    if request.method == "POST":
        userlivertest = Adduserlivertest(request.POST, request.FILES)
        if userlivertest.is_valid():
            Liver_function_test(user=user,alt=userlivertest.cleaned_data['alt'],ast=userlivertest.cleaned_data['ast'],alp=userlivertest.cleaned_data['alp'],
                                total_protein=userlivertest.cleaned_data['total_protein'],bilirubin=userlivertest.cleaned_data['bilirubin'],bilirubin_direct=userlivertest.cleaned_data['bilirubin_direct'],
                                ggt=userlivertest.cleaned_data['ggt'],liver_test_date=userlivertest.cleaned_data['liver_test_date'],
                                next_liver_test=userlivertest.cleaned_data['next_liver_test'],liver_scan=userlivertest.cleaned_data['liver_scan'],
                                docs_comments=userlivertest.cleaned_data['docs_comments']).save()
            messages.success(request, "Liver Test Added")

    userlivertest = Adduserlivertest()

    liverfunction = Liver_function_test.objects.filter(user=user)
    context = {'liverfunction':liverfunction, 'user':user, 'userlivertest':userlivertest}
    return render(request, "user-liver-function.html", context)


@login_required(login_url='accounts/signin')
def user_urinetest(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    if request.method == "POST":
        userurinetest = Adduserurinetest(request.POST, request.FILES)
        if userurinetest.is_valid():
            Urine_test(user=user,observation=userurinetest.cleaned_data['observation'],conclusion=userurinetest.cleaned_data['conclusion'],
                       urine_test_date=userurinetest.cleaned_data['urine_test_date'],next_urine_test=userurinetest.cleaned_data['next_urine_test']).save()
            messages.success(request, "Urine Test Added")

    userurinetest = Adduserurinetest()

    urinalysis = Urine_test.objects.filter(user=user)
    context = {'urinalysis':urinalysis, 'user':user, 'userurinetest':userurinetest}
    return render(request, "user-urine-test.html", context)

@login_required(login_url='accounts/signin')
def male_prostatetest(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)

    if request.method == "POST":
        maleprostatetest = Addprostatetest(request.POST, request.FILES)
        if maleprostatetest.is_valid():
            Prostate_specific_antigen(user=user, psa_total=maleprostatetest.cleaned_data['psa_total'], psa_test_date=maleprostatetest.cleaned_data['psa_test_date'],
                                      next_psa_test=maleprostatetest.cleaned_data['next_psa_test'], docs_comments=maleprostatetest.cleaned_data['docs_comments'],
                                      psa_scan=maleprostatetest.cleaned_data['psa_scan']).save()
            messages.success(request, "Prostate Test Added")

    maleprostatetest = Addprostatetest()

    prostatetest = Prostate_specific_antigen.objects.filter(user=user)
    context = {'prostatetest':prostatetest, 'user':user, 'maleprostatetest':maleprostatetest}
    return render(request, "male-prostate-test.html", context)

@login_required(login_url='accounts/signin')
def add_doctor(request):

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

            email = new_user_form.cleaned_data['email']
            mobile = new_user_form.cleaned_data['mobile']
            speciality = new_user_form.cleaned_data['speciality']
            hospital_name = new_user_form.cleaned_data['hospital_name']
            mdc_certificate = new_user_form.cleaned_data['mdc_certificate']
            # blood_group = new_user_form.cleaned_data['blood_group']
            # sickling_status = new_user_form.cleaned_data['sickling_status']
            # g6pd = new_user_form.cleaned_data['g6pd']

            pin = random.randint(1000,9999)

            now = datetime.datetime.now()

            try:
                user = User.objects.create_user(username=email, password=pin,)
                user.is_staff = True
                user.groups.add(Group.objects.get_or_create(name="Doctor")[0])
                user.save()

                user_info = AuthUserDemographic(user=user,email=email,picture=picture,
                                                title=title,first_name=first_name,other_name=other_name,
                                                surname=surname,sex=sex,date_of_birth=date_of_birth,
                                                nationality=nationality,religion=religion,
                                                marital_status=marital_status,address=address,
                                                mobile=mobile,speciality=speciality,hospital_name=hospital_name,
                                                mdc_certificate=mdc_certificate

                                                )


                user_info.save()

                user_info.unique_id = '{}{}{}{}{}'.format('D',now.day,now.month,
                                                        now.year,add_zeros(5,str(user_info.id)))

                user_info.save()

                sendsms(request,email,pin)



                messages.success(request, "Doctor added")
            except IntegrityError as e:
                # if 'unique constraint' in e.args[0]:
                    messages.error(request, 'User already exist')

        else:

            context = {'new_user_form':new_user_form}
            return render(request,'add_doctor.html',context)

    new_user_form = NewUserForm()
    context = {'new_user_form':new_user_form}
    return render(request,'add_doctor.html',context)

@login_required(login_url='accounts/signin')
def add_nurse(request):

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

            email = new_user_form.cleaned_data['email']
            mobile = new_user_form.cleaned_data['mobile']
            speciality = new_user_form.cleaned_data['speciality']
            mdc_certificate = new_user_form.cleaned_data['mdc_certificate']





            pin = random.randint(1000, 9999)

            now = datetime.datetime.now()

            try:
                user = User.objects.create_user(username=email, password=pin, )
                user.is_staff = True
                user.groups.add(Group.objects.get_or_create(name="Nurse")[0])
                user.save()

                user_info = AuthUserDemographic(user=user, email=email, picture=picture,
                                                title=title, first_name=first_name, other_name=other_name,
                                                surname=surname, sex=sex, date_of_birth=date_of_birth,
                                                nationality=nationality, religion=religion,
                                                marital_status=marital_status, address=address,
                                                mobile=mobile, speciality=speciality,
                                                mdc_certificate=mdc_certificate

                                                )

                user_info.save()

                user_info.unique_id = '{}{}{}{}{}'.format('N', now.day, now.month,
                                                          now.year, add_zeros(5, str(user_info.id)))

                user_info.save()

                sendsms(request, email, pin)

                messages.success(request, "Nurse added")
            except IntegrityError as e:
                # if 'unique constraint' in e.args[0]:
                messages.error(request, 'User already exist')

        else:

            context = {'new_user_form': new_user_form}
            return render(request, 'add_nurse.html', context)

    new_user_form = NewUserForm()
    context = {'new_user_form': new_user_form}
    return render(request, 'add_nurse.html', context)

@login_required(login_url='accounts/signin')
def add_general_supervisor(request):

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

            email = new_user_form.cleaned_data['email']
            mobile = new_user_form.cleaned_data['mobile']
            role = new_user_form.cleaned_data['role']


            pin = random.randint(1000, 9999)

            now = datetime.datetime.now()

            try:
                user = User.objects.create_user(username=email, password=pin, )
                user.is_staff = True

                user.groups.add(Group.objects.get_or_create(name="General Supervisor")[0])
                user.save()

                user_info = AuthUserDemographic(user=user, email=email, picture=picture,
                                                title=title, first_name=first_name, other_name=other_name,
                                                surname=surname, sex=sex, date_of_birth=date_of_birth,
                                                nationality=nationality, religion=religion,
                                                marital_status=marital_status, address=address,
                                                mobile=mobile, role=role,


                                                )

                user_info.save()

                user_info.unique_id = '{}{}{}{}{}'.format('GS', now.day, now.month,
                                                          now.year, add_zeros(5, str(user_info.id)))

                user_info.save()

                sendsms(request, email, pin)

                messages.success(request, "General Supervisor Added")
            except IntegrityError as e:
                # if 'unique constraint' in e.args[0]:
                messages.error(request, 'User already exist')

        else:
            print("Andrews")

        context = {'new_user_form': new_user_form}
        return render(request, 'add_supervisor.html', context)

    new_user_form = NewUserForm()
    context = {'new_user_form': new_user_form}
    return render(request, 'add_supervisor.html', context)

@login_required(login_url='accounts/signin')
def add_organization(request):

    if request.method == "POST":
        new_organization_form = Addorganization(request.POST, request.FILES)

        if new_organization_form.is_valid():
            type = new_organization_form.cleaned_data['type']
            name = new_organization_form.cleaned_data['name']
            address = new_organization_form.cleaned_data['address']
            reps_contact = new_organization_form.cleaned_data['reps_contact']
            reps_email = new_organization_form.cleaned_data['reps_email']

            try:
                organization_info = Organization(type=type, name=name, address=address, reps_contact=reps_contact,
                                                 reps_email=reps_email)
                organization_info.save()

                messages.success(request, "Organization Added")

            except IntegrityError as e:
                # if 'unique constraint' in e.args[0]:
                messages.error(request, 'Organization already exist')



        else:
            print('Andrews')

            context = {'new_organization_form':new_organization_form}
            return render(request, 'add_organization.html', context)

    new_organization_form = Addorganization()
    context = {'new_organization_form':new_organization_form}
    return render(request, 'add_organization.html', context)

@login_required(login_url='accounts/signin')
def add_partners(request):

    if request.method == "POST":
        new_user_form = NewPartnerForm(request.POST, request.FILES)

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

            email = new_user_form.cleaned_data['email']
            mobile = new_user_form.cleaned_data['mobile']
            role = new_user_form.cleaned_data['role']
            certificate = new_user_form.cleaned_data['certificate']
            organ = new_user_form.cleaned_data['organization']
            organization = Organization.objects.get(id=organ)



            pin = random.randint(1000, 9999)

            now = datetime.datetime.now()

            try:
                user = User.objects.create_user(username=email, password=pin, )
                user.is_staff = True
                user.groups.add(Group.objects.get_or_create(name="Partner")[0])
                user.save()

                user_info = Partners(user=user, email=email, picture=picture,
                                                title=title, first_name=first_name, other_name=other_name,
                                                surname=surname, sex=sex, date_of_birth=date_of_birth,
                                                nationality=nationality, religion=religion,
                                                marital_status=marital_status, address=address,
                                                mobile=mobile, role=role, certificate=certificate,
                                                organization=organization


                                                )

                user_info.save()

                user_info.unique_id = '{}{}{}{}{}'.format('PN', now.day, now.month,
                                                          now.year, add_zeros(5, str(user_info.id)))

                user_info.save()

                sendsms(request, mobile, pin)

                messages.success(request, "Partner Added")
            except IntegrityError as e:
                # if 'unique constraint' in e.args[0]:
                messages.error(request, 'Partner already exist')

        else:
            print("Andrews")

            context = {'new_user_form': new_user_form}
            return render(request, 'add_partner.html', context)

    new_user_form = NewPartnerForm()
    context = {'new_user_form': new_user_form}
    return render(request, 'add_partner.html', context)



@login_required(login_url='accounts/signin')
def patient_transfer(request,pk):
    user = AuthUserDemographic.objects.get(id=pk)
    patient_transfers = PatientPartnerTransfer.objects.all()

    if request.method == "POST":
        patienttransferform = PatientTransferForm(request.POST)

        if patienttransferform.is_valid():
            partner = patienttransferform.cleaned_data['partner']
            remark = patienttransferform.cleaned_data['remark']

            partnerauth = Partners.objects.get(id=partner)
            patrans = PatientPartnerTransfer(patient=user,partner=partnerauth,remark=remark)
            patrans.save()
            messages.success(request,"Patient Transfered to partner")
        else:
            context = {'patienttransferform': patienttransferform, 'user': user,
                       'patient_transfers': patient_transfers}
            return render(request, 'user_partner_transfer.html', context)

    patienttransferform = PatientTransferForm()
    context = {'patienttransferform': patienttransferform, 'user':user,
               'patient_transfers': patient_transfers}
    return render(request, 'user_partner_transfer.html', context)

@login_required(login_url='accounts/signin')
def partners_list(request):
    partner = Partners.objects.all()

    context = {'partner':partner}
    return render(request, 'partners_list.html', context)

@login_required(login_url='accounts/signin')
def doctors_list(request):
    user = AuthUserDemographic.objects.all()

    context = {'user_list':user}
    return render(request, 'doctors_list.html', context)

@login_required(login_url='accounts/signin')
def nurses_list(request):
    user = AuthUserDemographic.objects.all()

    context = {'user_list':user}
    return render(request, 'nurses_list.html', context)

@login_required(login_url='accounts/signin')
def partner_details(request,pk):
    partner = Partners.objects.get(id=pk)

    context = {'part': partner}
    return render(request, 'partner_details.html', context)

@login_required(login_url='accounts/signin')
def partner_view_patient(request,):
    partner=Partners.objects.get(user=request.user)
    user_list = PatientPartnerTransfer.objects.filter(partner=partner)

    context = {'user_list': user_list}
    return render(request, 'view_partner_patient.html', context)


@login_required(login_url='accounts/signin')
def organizations_list(request):
    organization = Organization.objects.all()

    context = {'organization':organization}
    return render(request, 'organizations_list.html', context)


@login_required(login_url='accounts/signin')
def supervisors_list(request):
    user = AuthUserDemographic.objects.all()

    context = {'user_list': user}
    return render(request, 'supervisors_list.html', context)


@login_required(login_url='accounts/signin')
def add_drugs(request):

    if request.method == "POST":
        new_drug_form = Adddrugform(request.POST)

        if new_drug_form.is_valid():
            name = new_drug_form.cleaned_data['name']

            try:
                drug_info = Drugs(name=name)
                drug_info.save()

                messages.success(request, "Drug Added")

            except IntegrityError as e:
                # if 'unique constraint' in e.args[0]:
                messages.error(request, 'Drug already exist')

        else:
            print("Sam")

            context = {'new_drug_form': new_drug_form}
            return render(request, 'add_drugs.html', context)

    new_drug_form = Adddrugform()
    context = {'new_drug_form':new_drug_form}
    return render(request, 'add_drugs.html', context)










