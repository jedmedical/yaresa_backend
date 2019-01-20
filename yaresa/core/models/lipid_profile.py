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
    lipid_profile_date = models.DateField()
    next_lipid_test = models.DateField()
    lipid_scan = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    docs_comments = models.CharField(max_length=3000, null=True)

    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.lipid_scan.url)


