from core.models import AuthUserDemographic
from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models
from yaresa import settings


__author__ = 'sam'


class Full_blood_count(BaseModel):
    user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE)
    fbc_image_scan = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    red_blood_cell = models.CharField(max_length=255, null=True)
    hemoglobin = models.CharField(max_length=255, null=True)
    hematocrit = models.CharField(max_length=255, null=True)
    white_blood_cell = models.CharField(max_length=255, null=True)
    platelet = models.CharField(max_length=255, null=True)
    neutrophil = models.CharField(max_length=255, null=True)
    lymphocyte = models.CharField(max_length=255, null=True)
    full_blood_count_date = models.DateField()
    next_full_blood_count_date = models.DateField(null=True)
    docs_comments = models.CharField(max_length=3000, null=True)

    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.fbc_image_scan.url)


