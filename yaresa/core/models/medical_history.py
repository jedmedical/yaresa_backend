from core.models.auth_user_demographic import AuthUserDemographic
from django.db import models

__author__ = 'andrews'

class Medical_history(models.Model):
    user = models.OneToOneField(AuthUserDemographic,on_delete=models.CASCADE, null=True)
    diabetes_mellitus = models.BooleanField(default=False)
    systematic_hypertension  = models.BooleanField(default=False)
    epilepsy = models.BooleanField(default=False)
    others = models.CharField(max_length=300,null=True)


