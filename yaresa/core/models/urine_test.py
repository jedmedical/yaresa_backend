from core.models import AuthUserDemographic
from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models


__author__ = 'sam'


class Urine_test(BaseModel):
    user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE)
    leukocytes = models.CharField(max_length=255, null=True)
    nitrites = models.CharField(max_length=255, null=True)
    urobilinogen = models.CharField(max_length=255, null=True)
    protein = models.CharField(max_length=255, null=True)
    ph_level = models.CharField(max_length=255, null=True)
    blood_urine = models.CharField(max_length=255, null=True)
    specific_gravity_test = models.CharField(max_length=255, null=True)
    ketone = models.CharField(max_length=255, null=True)
    bilirubin = models.CharField(max_length=255, null=True)
    glucose = models.CharField(max_length=255, null=True)
    date = models.DateField()


