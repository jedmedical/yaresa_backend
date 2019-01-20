from core.models import AuthUserDemographic
from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models


__author__ = 'sam'


class Urine_test(BaseModel):
    user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE)
    observation = models.CharField(max_length=5000, null=True)
    conclusion = models.CharField(max_length=5000, null=True)
    urine_test_date = models.DateField()
    next_urine_test = models.DateField(null=True)


