from django.db import models
from base.models import *


class PoliceModel(BaseUser):
    rank = models.CharField(max_length=10)
    profile_img = models.ImageField(upload_to="police_profile", height_field=None, width_field=None, max_length=None, null=True, blank=True)


class PoliceHeadModel(BaseUser):
    rank = models.CharField(max_length=10)
    profile_img = models.ImageField(upload_to="police_admin_profile", height_field=None, width_field=None, max_length=None, null=True, blank=True)


class AddPoliceModel(BaseModel):
    file = models.FileField(upload_to="police_excel", max_length=100)


class AddPoliceAdminModel(BaseModel):
    file = models.FileField(upload_to="police_admin_excel", max_length=100)