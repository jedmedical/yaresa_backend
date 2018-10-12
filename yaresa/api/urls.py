from django.conf.urls import url

from api.views import signin

__author__ = 'andrews'

app_name = "core"
urlpatterns = [
        url(r'^accounts/signin', signin, name="signin"),
]