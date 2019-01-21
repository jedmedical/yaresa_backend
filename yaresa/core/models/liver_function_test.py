from core.models import AuthUserDemographic
from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models
from yaresa import settings


__author__ = 'sam'


class Liver_function_test(BaseModel):
    user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE)
    alt = models.CharField(max_length=255, null=True)
    ast = models.CharField(max_length=255, null=True)
    alp = models.CharField(max_length=255, null=True)
    total_protein = models.CharField(max_length=255, null=True)
    bilirubin = models.CharField(max_length=255, null=True)
    bilirubin_direct = models.CharField(max_length=255, null=True)
    ggt = models.CharField(max_length=255, null=True)
    liver_test_date = models.DateField()
    next_liver_test = models.DateField()
    liver_scan = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    docs_comments = models.CharField(max_length=3000, null=True)

    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.liver_scan.url)
