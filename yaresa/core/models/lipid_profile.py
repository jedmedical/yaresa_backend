from core.models import AuthUserDemographic
from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models
from yaresa import settings


__author__ = 'sam'


class Lipid_profile(BaseModel):
    user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE)
    total_cholesterol = models.CharField(max_length=255, null=True)
    hdl_cholesterol = models.CharField(max_length=255, null=True)
    ldl_cholesterol = models.CharField(max_length=255, null=True)
    triglycerides = models.CharField(max_length=255, null=True)
    date = models.DateField()
    next_lipid_test = models.DateField()
    lipid_scan = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')


