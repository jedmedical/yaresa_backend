from core.models import AuthUserDemographic
from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models


__author__ = 'sam'

class Drugs(models.Model):
    name = models.CharField(max_length=255, null=True)



    def __str__(self):
        return '{}'.format(self.name,)
