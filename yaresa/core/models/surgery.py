from core.models import AuthUserDemographic
from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models


__author__ = 'sam'

class Surgery(BaseModel):
    user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=True)
    doctor = models.CharField(max_length=255, null=True)
    hospital = models.CharField(max_length=255, null=True)
    date = models.DateField()
