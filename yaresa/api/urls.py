from django.conf.urls import url

from api.views import signin, reset_pin

__author__ = 'andrews'

app_name = "core"
urlpatterns = [
        url(r'^accounts/signin', signin, name="signin"),
        url(r'^accounts/reset-password', reset_pin, name="reset-password"),
]