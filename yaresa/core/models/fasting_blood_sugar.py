from core.models import AuthUserDemographic
from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models


__author__ = 'sam'


class Fasting_blood_sugar(BaseModel):
    user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE)
    test_result = models.CharField(max_length=255, null=True)
    saved_result = models.CharField(max_length=255, null=True)
    docs_comments = models.CharField(max_length=3000, null=True)
    test_date = models.DateField()
    next_fbs_test = models.DateField(null=True)
