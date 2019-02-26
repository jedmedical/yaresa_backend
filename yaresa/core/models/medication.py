from core.models import AuthUserDemographic
from core.models.drugs import Drugs
from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models


__author__ = 'sam'

class Medication(BaseModel):
    user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Drugs, on_delete=models.CASCADE ,null=True)
    dosage = models.CharField(max_length=255,null=True)
    strength = models.CharField(max_length=30, null=True)
    refill_date = models.DateField()

    def __str__(self):
        return '{}'.format(self.medicine)
