from django.conf.urls import url

from api.views import signin, reset_pin, get_summary, get_profile, get_medigraph, get_socialhistory, get_allergy_list, \
        get_medical_history_list, get_medication_list, get_surgery_list, get_bmi, get_bp_list

__author__ = 'andrews'

app_name = "core"
urlpatterns = [
        url(r'^accounts/signin', signin, name="signin"),
        url(r'^accounts/reset-password', reset_pin, name="reset-password"),
        url(r'^get-summary', get_summary, name="summary"),
        url(r'^get-profile', get_profile, name="profile"),
        url(r'^get-social-history', get_socialhistory, name="social-history"),
        url(r'^get-medi-graph', get_medigraph, name="medigraph"),
        url(r'^get-allergy-list', get_allergy_list, name="allergy-list"),
        url(r'^get-medical-history-list', get_medical_history_list, name="medical-history-list"),
        url(r'^get-medication-list', get_medication_list, name="medication-list"),
        url(r'^get-surgery-list',get_surgery_list, name="surgery-list"),
        url(r'^get-bmi', get_bmi, name="bmi"),
        url(r'^get-bp-list', get_bp_list, name="bp-list"),


]