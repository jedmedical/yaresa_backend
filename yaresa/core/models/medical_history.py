from core.models.auth_user_demographic import AuthUserDemographic
from core.models.base_model import BaseModel
from django.db import models

__author__ = 'andrews'

class Medical_history(BaseModel):
    user = models.OneToOneField(AuthUserDemographic,on_delete=models.CASCADE, null=True)
    # diabetes_mellitus = models.BooleanField(default=False)
    # systematic_hypertension  = models.BooleanField(default=False)
    # epilepsy = models.BooleanField(default=False)
    #
    condition = models.CharField(max_length=255,null=True)
    condition_active = models.BooleanField(default=False)




