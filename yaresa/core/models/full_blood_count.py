from core.models import AuthUserDemographic
from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models
from yaresa import settings


__author__ = 'sam'


class Full_blood_count(BaseModel):
    user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE)
    test_scan = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    red_blood_cell = models.CharField(max_length=255, null=True)
    hemoglobin = models.CharField(max_length=255, null=True)
    hematocrit = models.CharField(max_length=255, null=True)
    white_blood_cell = models.CharField(max_length=255, null=True)
    platelet = models.CharField(max_length=255, null=True)
    neutrophil = models.CharField(max_length=255, null=True)
    lymphocyte = models.CharField(max_length=255, null=True)
    date = models.DateField()
    next_test_date = models.DateField(null=True)


