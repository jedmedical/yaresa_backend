from core.models.auth_user_demographic import AuthUserDemographic
from django.contrib.auth.models import User
from django.db import models

__author__ = 'andrews'

class Height(models.Model):
    user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE)
    height = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Weight(models.Model):
    user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE)
    weight = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Blood_Pressure(models.Model):
    user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE)
    bp = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)




