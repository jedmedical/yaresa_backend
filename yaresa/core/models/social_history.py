from core.models.auth_user_demographic import AuthUserDemographic
from core.models.base_model import BaseModel
from django.db import models

__author__ = 'andrews'

class Social_history(BaseModel):
    user = models.OneToOneField(AuthUserDemographic, on_delete=models.CASCADE, null=True)
    alcohol = models.BooleanField(default=False)
    smoking  = models.BooleanField(default=False)

