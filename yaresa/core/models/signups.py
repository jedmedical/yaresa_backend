__author__ = 'andrews'
from django.db import models

class Signup(models.Model):

    first_name = models.CharField(max_length=255,null=True,verbose_name="first_name")
    last_name = models.CharField(max_length=255,null=True,verbose_name="Lastname")
    email = models.EmailField(max_length=255,null=True,verbose_name="Email")
    phone = models.CharField(max_length=255,null=True,verbose_name="Phone")
    registered = models.BooleanField(default=False)

