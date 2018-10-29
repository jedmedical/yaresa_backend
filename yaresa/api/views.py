import json
from core.models import AuthUserDemographic, Blood_Pressure, Height, Weight, Med_graphic, Social_history
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        if username and password:

            user = authenticate(request, username=username, password=password)

            if user is not None:
                    user_serial = AuthUserDemographic.objects.get(user= user)



                    response = json.dumps({'status': 'ok', 'user_id': user_serial.id,
                                           'first_time':user_serial.first_login, "name":user_serial.first_name,
                                           'accnum':user_serial.unique_id})

            else:
                    response = json.dumps({'status': 'error', 'result': "Wrong username or password"})
        else:
            response = json.dumps({'status': 'error', 'result': "Username or password not provided"})

    else:
        response = json.dumps({'status': 'error', 'result': "something went wrong"})

    return HttpResponse(response, content_type='application/json')

@csrf_exempt
def reset_pin(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id','')
        password = request.POST.get('password','')

        if user_id and password:
            demoUser = AuthUserDemographic.objects.get(id=user_id)
            user = demoUser.user
            user.set_password(password)
            user.save()
            demoUser.first_login = False
            demoUser.save()

            response = json.dumps({'status': 'ok', })

        else:
                    response = json.dumps({'status': 'error', 'result': "Invalid data"})

    else:
        response = json.dumps({'status': 'error', 'result': "something went wrong"})

    return HttpResponse(response, content_type='application/json')

@csrf_exempt
def get_summary(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id','')


        if user_id :
            demoUser = AuthUserDemographic.objects.get(id=user_id)

            bp = Blood_Pressure.objects.filter(user=demoUser)
            if bp:
                bp = bp.order_by('-id')[0]
                bp = bp.bp
            else:
                bp = "Unknown"

            height = Height.objects.filter(user=demoUser)
            if height:
                height = height.order_by('-id')[0]

                weight = Weight.objects.filter(user=demoUser)
                if weight:
                    weight= weight.order_by('-id')[0]
                    print(weight.weight)
                    print(height.height)
                    bmi = eval(weight.weight)/eval(height.height)
                else:
                    bmi = "unknown"
            else:
                bmi = "unknown"






            demoUser.save()

            response = json.dumps({'status': 'ok',"profile_pic":demoUser.picture.path,"bp":str(bp),"bmi":str(bmi), })

        else:
                    response = json.dumps({'status': 'error', 'result': "Invalid data"})

    else:
        response = json.dumps({'status': 'error', 'result': "something went wrong"})

    return HttpResponse(response, content_type='application/json')


@csrf_exempt
def get_profile(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id','')


        if user_id :
            demoUser = AuthUserDemographic.objects.get(id=user_id)

            response = json.dumps({'status': 'ok',"profile_pic":demoUser.picture.path,"name":"{} {}".format(demoUser.first_name,demoUser.surname),
                                   "address":demoUser.address,"sex":demoUser.sex,"mstat":demoUser.marital_status,"email":demoUser.email,
                                   "mobile":demoUser.mobile,"occu":demoUser.occupation, "nationality":demoUser.nationality,"dob":str(demoUser.date_of_birth),
                                   "religion":demoUser.religion,"acc":demoUser.unique_id})

        else:
                    response = json.dumps({'status': 'error', 'result': "Invalid data"})

    else:
        response = json.dumps({'status': 'error', 'result': "something went wrong"})

    return HttpResponse(response, content_type='application/json')

@csrf_exempt
def get_medigraph(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id','')


        if user_id :
            demoUser = AuthUserDemographic.objects.get(id=user_id)
            medigraph = Med_graphic.objects.filter(user=demoUser)
            if medigraph:
                medigraph = medigraph[0]

                response = json.dumps({'status': 'ok',"bg":medigraph.blood_group,"ss":medigraph.sickling_status,
                                       "gs":medigraph.g6pd_status})
            else:
                response = json.dumps({'status': 'error', 'result': "No record found"})



        else:
                    response = json.dumps({'status': 'error', 'result': "Invalid data"})

    else:
        response = json.dumps({'status': 'error', 'result': "something went wrong"})

    return HttpResponse(response, content_type='application/json')


@csrf_exempt
def get_socialhistory(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id','')


        if user_id :
            demoUser = AuthUserDemographic.objects.get(id=user_id)
            social = Social_history.objects.filter(user=demoUser)
            if social:
                social = social[0]
                smoke = "No"
                alcohol = "No"
                if social.smoking:
                    smoke = "Yes"

                if social.alcohol:
                    alcohol = "Yes"


                response = json.dumps({'status': 'ok',"smoke":smoke,"alcohol":alcohol
                                       })
            else:
                response = json.dumps({'status': 'error', 'result': "No record found"})



        else:
                    response = json.dumps({'status': 'error', 'result': "Invalid data"})

    else:
        response = json.dumps({'status': 'error', 'result': "something went wrong"})

    return HttpResponse(response, content_type='application/json')
