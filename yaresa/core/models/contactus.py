from django.db import models

__author__ = 'sam'

class Contactus(models.Model):
    yourname = models.CharField(max_length=255,null=True)
    youremail = models.CharField(max_length=255,null=True)
    yournumber = models.CharField(max_length=255,null=True)
    subject = models.CharField(max_length=255,null=True)
    message = models.CharField(max_length=1500,null=True)

