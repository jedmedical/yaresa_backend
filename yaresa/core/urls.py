from core.views.core_view import dashboard, add_new_user, add_medical_info
from core.views.home_views import index, signin
from django.conf.urls import url

__author__ = 'andrews'



app_name="core"
urlpatterns = [
    url(r'^$', index, name="home"),

    url(r'^accounts/signin', signin, name="signin"),
    url(r'^dashboard', dashboard, name="dashboard"),
    url(r'^add-user', add_new_user, name="new-user"),
    url(r'^add-medi-info/(?P<pk>\d+)', add_medical_info, name="add-medi-info"),


]