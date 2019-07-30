from core.views.core_view import dashboard, add_new_user, add_medical_info, user_list, user_detail, user_condition, \
    user_allergy, user_medication, user_account_reset, blood_group_count, sickling_count, user_bloodpressure, \
    user_bmi, g6pd_count, user_surgery, user_fastbloodsugar, user_fullbloodcount, user_lipidprofile, user_renaltest, \
    user_livertest, male_prostatetest, user_urinetest, add_doctor, add_nurse, add_general_supervisor, add_organization, \
    add_partners, doctorpatients_list, patient_transfer, partners_list, doctors_list, nurses_list, partner_details, \
    partner_view_patient, organizations_list, supervisors_list, add_drugs, add_conditions

from core.views.home_views import index, signin, sign_out
from django.conf.urls import url

__author__ = 'andrews'



app_name="core"
urlpatterns = [
    url(r'^$', index, name="home"),

    url(r'^accounts/signin', signin, name="signin"),
    url(r'^accounts/signout', sign_out, name="signout"),
    url(r'^dashboard', dashboard, name="dashboard"),
    url(r'^user-list', user_list, name="user-list"),
    url(r'^doctors-list', doctors_list , name="doctors-list"),
    url(r'^nurses-list', nurses_list, name="nurses-list"),
    url(r'^partner-list', partners_list, name="partners-list"),
    url(r'^supervisors-list', supervisors_list, name="supervisors-list"),
    url(r'^doctor-patients-list', doctorpatients_list, name="doctor-patients-list"),
    url(r'^add-user', add_new_user, name="new-user"),
    url(r'^user-account-reset/(?P<pk>\d+)', user_account_reset, name="user-account-medication"),
    url(r'^add-medi-info/(?P<pk>\d+)', add_medical_info, name="add-medi-info"),
    url(r'^user-detail/(?P<pk>\d+)', user_detail, name="user-detail"),
    url(r'^partner-detail/(?P<pk>\d+)', partner_details, name="partner-detail"),
    url(r'^user-condition/(?P<pk>\d+)', user_condition, name="user-condition"),
    url(r'^user-allergy/(?P<pk>\d+)', user_allergy, name="user-allergy"),
    url(r'^user-medication/(?P<pk>\d+)', user_medication, name="user-medication"),
    url(r'^user-bmi/(?P<pk>\d+)', user_bmi, name="user-bmi"),
    url(r'^user-bloodpressure/(?P<pk>\d+)', user_bloodpressure, name="user-bloodpressure"),
    url(r'^user-surgery/(?P<pk>\d+)', user_surgery, name="user-surgery"),
    url(r'^user-fasting-blood-sugar/(?P<pk>\d+)', user_fastbloodsugar, name="user-fastbloodsugar"),
    url(r'^user-full-blood-count/(?P<pk>\d+)', user_fullbloodcount, name="user-fullbloodcount"),
    url(r'^user-lipid-profile/(?P<pk>\d+)', user_lipidprofile, name="user-lipidprofile"),
    url(r'^user-renal-function/(?P<pk>\d+)', user_renaltest, name="user-renalfunction"),
    url(r'^user-liver-function/(?P<pk>\d+)', user_livertest, name="user-liverfunction"),
    url(r'^user-urine-test/(?P<pk>\d+)', user_urinetest, name="user-urinetest"),
    url(r'^user-prostate-test/(?P<pk>\d+)', male_prostatetest, name="male-prostatetest"),



    url(r'^blood-group-count', blood_group_count, name="blood-group-count"),
    url(r'^sickling-status-count', sickling_count, name="sickling-count"),
    url(r'^g6pd-count', g6pd_count, name="g6pd-count"),

    url(r'^add-doctor', add_doctor, name="new-doctor"),
    url(r'^add-nurse', add_nurse, name="new-nurse"),
    url(r'^add-general-supervisor', add_general_supervisor, name="new-generalsupervisor"),
    url(r'^add-organization', add_organization, name="new-organization"),
    url(r'^add-partner', add_partners, name="new-partner"),

    url(r'^patient-transfer/(?P<pk>\d+)', patient_transfer, name="patient-transfer"),
    url(r'^partner-patient', partner_view_patient, name="partner-view-patient"),
    url(r'^organizations-list', organizations_list , name="organizations-list"),

    url(r'^add-drugs', add_drugs, name="new-drug"),
    url(r'^add-conditions', add_conditions, name="new-condition"),

]