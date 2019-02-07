from core.models import Partners, AuthUserDemographic
from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models

class PatientPartnerTransfer(BaseModel):
    patient = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE, null=True, related_name="patient")
    partner = models.ForeignKey(Partners, on_delete=models.CASCADE, null=True, related_name="partner")
    created_by = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE, null=True, related_name="created_by")
    remark = models.CharField(max_length = 200,null=True)
    status = models.CharField(max_length = 30,null=True,default="Active")

