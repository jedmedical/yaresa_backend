from django.shortcuts import render

from core.models import Logging


def my_activities(request):

    context = {'my_activities': Logging.get_logs_for_user(request.user.id)}
    return render(request, 'logging/my_activities.html', context)
