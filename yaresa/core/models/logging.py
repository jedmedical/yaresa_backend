from django.db import models

from core.models import AuthUserDemographic
from core.models.base_model import BaseModel


class Logging(BaseModel):
    actor = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE,related_name="actor")
    affected_user = models.ForeignKey(AuthUserDemographic, on_delete=models.CASCADE)
    action = models.CharField(max_length= 200,null=True)
    reference_db = models.CharField(max_length=255,null=True)

    @classmethod
    def create_logging(cls,actor_id,affected_user_id,action,reference_db):
        log = cls(actor=AuthUserDemographic.get_auth_user_by_id(actor_id),
                  affected_user=AuthUserDemographic.get_auth_user_by_id(affected_user_id),
                  action=action,reference_db=reference_db)
        return log.save()

    @classmethod
    def get_logs_for_user(cls,id):
        return cls.objects.filter(actor=AuthUserDemographic.get_auth_user_by_id(id))
