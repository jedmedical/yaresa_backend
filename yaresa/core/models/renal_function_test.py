from core.models import AuthUserDemographic
from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models
from yaresa import settings


__author__ = 'sam'

class Renal_function_test(BaseModel):
    user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE)
    creatinine = models.CharField(max_length=255, null=True)
    urea = models.CharField(max_length=255, null=True)
    gfr = models.CharField(max_length=255, null=True)
    renal_test_date = models.DateField()
    next_renal_test = models.DateField()
    renal_scan = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    docs_comments = models.CharField(max_length=3000, null=True)

    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.renal_scan.url)




