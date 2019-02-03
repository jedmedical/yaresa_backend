from core.models.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from yaresa import settings

sex = (("Male", "MALE"), ("Female", "FEMALE"))
marital = (("Married", "MARRIED"), ("Single", "SINGLE"))
class Partners(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    picture = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    title = models.CharField(max_length= 30,null=True)
    first_name = models.CharField(max_length=255,null=True)
    other_name = models.CharField(max_length=255,null=True)
    unique_id = models.CharField(max_length=255,null=True)
    surname = models.CharField(max_length=255,null=True,verbose_name="Surname")
    sex = models.CharField(max_length=255,choices=sex,verbose_name="Gender",default="Male")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    nationality = models.CharField(max_length=255,null=True)
    religion = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=255,null=True)
    first_login = models.BooleanField(default=True)
    speciality = models.CharField(max_length=255,null=True)
    facility_name = models.CharField(max_length=255,null=True)
    certificate = models.CharField(max_length=255,null=True)
    role = models.CharField(max_length=225,null=True)


    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.picture.url)





