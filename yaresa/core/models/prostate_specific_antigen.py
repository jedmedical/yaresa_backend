from core.models import AuthUserDemographic
from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models
from yaresa import settings


__author__ = 'sam'


class Prostate_specific_antigen(BaseModel):
    user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE)
    psa_total = models.CharField(max_length=255, null=True)
    docs_comments = models.CharField(max_length=3000, null=True)
    psa_test_date = models.DateField()
    next_psa_test = models.DateField()
    psa_scan = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.psa_scan.url)
