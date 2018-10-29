from django.conf.urls import url

from api.views import signin, reset_pin, get_summary, get_profile, get_medigraph, get_socialhistory

__author__ = 'andrews'

app_name = "core"
urlpatterns = [
        url(r'^accounts/signin', signin, name="signin"),
        url(r'^accounts/reset-password', reset_pin, name="reset-password"),
        url(r'^get-summary', get_summary, name="summary"),
        url(r'^get-profile', get_profile, name="profile"),
        url(r'^get-social-history', get_socialhistory, name="social-history"),
        url(r'^get-medi-graph', get_medigraph, name="medigraph"),

]