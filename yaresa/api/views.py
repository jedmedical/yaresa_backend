import json
from core.models import AuthUserDemographic
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



                    response = json.dumps({'status': 'ok', 'user_id': user_serial.id,'first_time':user_serial.first_login})

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
