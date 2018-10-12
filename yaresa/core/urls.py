from core.views.core_view import dashboard, add_new_user, add_medical_info, user_list, user_detail, user_condition, \
    user_allergy
from core.views.home_views import index, signin
from django.conf.urls import url

__author__ = 'andrews'



app_name="core"
urlpatterns = [
    url(r'^$', index, name="home"),

    url(r'^accounts/signin', signin, name="signin"),
    url(r'^dashboard', dashboard, name="dashboard"),
    url(r'^user-list', user_list, name="user-list"),
    url(r'^add-user', add_new_user, name="new-user"),
    url(r'^add-medi-info/(?P<pk>\d+)', add_medical_info, name="add-medi-info"),
    url(r'^user-detail/(?P<pk>\d+)', user_detail, name="user-detail"),
    url(r'^user-condition/(?P<pk>\d+)', user_condition, name="user-condition"),
    url(r'^user-allergy/(?P<pk>\d+)', user_allergy, name="user-allergy"),


]