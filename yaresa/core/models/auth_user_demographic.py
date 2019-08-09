from core.core_util import get_object_or_none
from core.models.base_model import BaseModel
from django.contrib.auth.models import User, Group
from django.db import models
from datetime import date
# Create your models here.
from yaresa import settings

sex = (("Male", "MALE"), ("Female", "FEMALE"))
marital = (("Married", "MARRIED"), ("Single", "SINGLE"), ("Divorced", "DIVORCED"), ("Widowed", "WIDOWED"))
religion = (("Christianity","Christianity"),("Islam","Islam"),("Traditional","Traditional"),("Other","Other"),("None","None"))
region_of_residence = (("Ahafo Region","Ahafo Region"),("Ashanti Region","Ashanti Region"),("Bono East Region","Bono East Region"),
                       ("Bono Region","Bono Region"),("Central Region","Central Region"),("Eastern Region","Eastern Region"),
                       ("Greater Accra Region","Greater Accra Region"),("Northern Region","Northern Region"),("North East Region","North East Region"),
                       ("Oti Region","Oti Region"),("Savannah Region","Savannah Region"),("Upper East Region","Upper East Region"),
                       ("Upper West Region","Upper West Region"),("Volta Region","Volta Region"),("Western Region","Western Region"),
                       ("Western North Region","Western North Region"))

class AuthUserDemographic(BaseModel):
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
    religion = models.CharField(max_length=255,choices=religion,null=True)
    marital_status = models.CharField(max_length=255,choices=marital,default="Single")
    address = models.CharField(max_length=255,blank=True,null=True)
    occupation = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=255,null=True)
    emergency_contact_name = models.CharField(max_length=255,null=True)
    emergency_contact_mobile = models.CharField(max_length=255,null=True)
    emergency_contact_address = models.CharField(max_length=255, null=True)
    emergency_contact_email = models.EmailField(null=True)
    first_login = models.BooleanField(default=True)
    speciality = models.CharField(max_length=255,null=True)
    hospital_name = models.CharField(max_length=255,null=True)
    mdc_certificate = models.CharField(max_length=255,null=True)
    role = models.CharField(max_length=225,null=True)
    denomination = models.CharField(max_length=225,null=True)
    region_of_residence = models.CharField(max_length=255,choices=region_of_residence,null=True)
    city_and_town = models.CharField(max_length=225,null=True)

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.other_name, self.surname)

    def is_patient(self, ):
        users_in_group = Group.objects.get(name="Patient").user_set.all()
        return True if self.user in users_in_group else False

    def is_doctor(self, ):
        users_in_group = Group.objects.get(name="Doctor").user_set.all()
        return True if self.user in users_in_group else False

    def is_nurse(self, ):
        users_in_group = Group.objects.get(name="Nurse").user_set.all()
        return True if self.user in users_in_group else False

    def is_generalsupervisor(self, ):
        users_in_group = Group.objects.get(name="General Supervisor").user_set.all()
        return True if self.user in users_in_group else False


    def get_age(self):
        born = self.date_of_birth
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.picture.url)

    @classmethod
    def get_auth_user_by_id(cls,id):
        user = get_object_or_none(User,id=id)
        return get_object_or_none(cls,user=user)








