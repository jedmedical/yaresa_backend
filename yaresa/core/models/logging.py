from django.db import models

from core.models import AuthUserDemographic
from core.models.base_model import BaseModel


class Logging(BaseModel):
    actor = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE,related_name="actor")
    affected_user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE)
    action = models.CharField(max_length= 200,null=True)
    reference_db = models.CharField(max_length=255,null=True)