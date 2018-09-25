from core.models.auth_user_demographic import AuthUserDemographic
from django.contrib.auth.models import User
from django.db import models

__author__ = 'andrews'

bloodgroup = (("A+","A+"),("A-","A-"),("B+","B+"),("AB+","AB+"),("AB-","AB-"),("O+","O+"),("O-","O-"))
sickling = (("AA","AA"),("AS","AS"),("SS","SS"),("SC","SC"))
g6pd = (("Normal","Normal"),("Partial Defect","Partial Defect"),("Full Defect","Full Defect"))


class Med_graphic(models.Model):
    user = models.OneToOneField(AuthUserDemographic, on_delete=models.CASCADE, null=True)
    blood_group = models.CharField(choices=bloodgroup,max_length=255,null=True)
    sickling_status = models.CharField(choices=sickling,max_length=255,null=True)
    g6pd_status = models.CharField(choices=g6pd,max_length=255,null=True)
