from core.models import AuthUserDemographic
from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models


__author__ = 'sam'


class Organization(models.Model):
    type = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    telephone = models.CharField(max_length=255, null=True)

         