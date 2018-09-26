from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
sex = (("Male", "MALE"), ("Female", "FEMALE"))
marital = (("Married", "MARRIED"), ("Single", "SINGLE"))
class AuthUserDemographic(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=255,null=True)
    unique_id = models.CharField(max_length=255,null=True)
    surname = models.CharField(max_length=255,null=True,verbose_name="Surname")
    sex = models.CharField(max_length=255,choices=sex,verbose_name="Gender",default="Male")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    nationality = models.CharField(max_length=255,null=True)
    religion = models.CharField(max_length=255,null=True)
    marital_status = models.CharField(max_length=255,choices=marital,default="Single")
    address = models.CharField(max_length=255,null=True)
    occupation = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=255,null=True)
    emergency_contact_name = models.CharField(max_length=255,null=True)
    emergency_contact_mobile = models.CharField(max_length=255,null=True)





