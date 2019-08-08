from core.models import AuthUserDemographic
from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models


__author__ = 'sam'


class Organization(models.Model):
    type = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    reps_contact = models.CharField(max_length=255, null=True)
    reps_email = models.CharField(max_length=255, null=True)


    def __str__(self):
        return '{} {}'.format(self.type, self.name)