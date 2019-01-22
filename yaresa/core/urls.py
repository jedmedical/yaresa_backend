from core.views.core_view import dashboard, add_new_user, add_medical_info, user_list, user_detail, user_condition, \
    user_allergy, user_medication, user_account_reset, blood_group_count, sickling_count, user_bloodpressure, \
    user_bmi, g6pd_count, user_surgery, user_fastbloodsugar, user_fullbloodcount, user_lipidprofile, add_doctor, \
    add_nurse, add_general_supervisor
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
    url(r'^user-account-reset/(?P<pk>\d+)', user_account_reset, name="user-account-medication"),
    url(r'^add-medi-info/(?P<pk>\d+)', add_medical_info, name="add-medi-info"),
    url(r'^user-detail/(?P<pk>\d+)', user_detail, name="user-detail"),
    url(r'^user-condition/(?P<pk>\d+)', user_condition, name="user-condition"),
    url(r'^user-allergy/(?P<pk>\d+)', user_allergy, name="user-allergy"),
    url(r'^user-medication/(?P<pk>\d+)', user_medication, name="user-medication"),
    url(r'^user-bmi/(?P<pk>\d+)', user_bmi, name="user-bmi"),
    url(r'^user-bloodpressure/(?P<pk>\d+)', user_bloodpressure, name="user-bloodpressure"),
    url(r'^user-surgery/(?P<pk>\d+)', user_surgery, name="user-surgery"),
    url(r'^user-fasting-blood-sugar/(?P<pk>\d+)', user_fastbloodsugar, name="user-fastbloodsugar"),
    url(r'^user-full-blood-count/(?P<pk>\d+)', user_fullbloodcount, name="user-fullbloodcount"),
    url(r'^user-lipid-profile/(?P<pk>\d+)', user_lipidprofile, name="user-lipidprofile"),


    url(r'^blood-group-count', blood_group_count, name="blood-group-count"),
    url(r'^sickling-status-count', sickling_count, name="sickling-count"),
    url(r'^g6pd-count', g6pd_count, name="g6pd-count"),

    url(r'^add-doctor', add_doctor, name="new-doctor"),
    url(r'^add-nurse', add_nurse, name="new-nurse"),
    url(r'^add-general-supervisor', add_general_supervisor, name="new-generalsupervisor"),


]