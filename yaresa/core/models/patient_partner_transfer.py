from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models

class PatientPartnerTransfer(BaseModel):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    partner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    remark = models.CharField(max_length = 200,null=True)
    status = models.CharField(max_length = 30,null=True)

