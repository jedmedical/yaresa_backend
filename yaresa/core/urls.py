from core.views.home_views import index
from django.conf.urls import url

__author__ = 'andrews'



app_name="core"
urlpatterns = [
    url(r'^$', index, name="home"),
    # url(r'^dashboard', dashboard, name="dashboard"),
]