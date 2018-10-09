from core.models import AuthUserDemographic
from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models

class Medication(BaseModel):
    user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE)
    medicine = models.CharField(max_length=255,null=True)
    dosage = models.CharField(max_length=255,null=True)
    refill_date = models.DateField()
