from core.views.core_views import dashboard
from core.views.home_views import index, signin
from django.conf.urls import url

__author__ = 'andrews'



app_name="core"
urlpatterns = [
    url(r'^$', index, name="home"),

    url(r'^accounts/signin', signin, name="signin"),
    url(r'^dashboard', dashboard, name="dashboard"),
    url(r'^add-user', dashboard, name="dashboard"),

]