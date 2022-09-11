from datetime import date
from email.policy import default
from django.db import models
from base.models import BaseModel
from .validators import *

GENDER = (("MALE", "MALE"), ("FEMALE", "FEMALE"), ("OTHERS", "OTHERS"))

PERSON_SELECTOR = (("MEN", "MEN"), ("WOMEN", "WOMEN"), ("CHILD", "CHILD"), ("OTHER", "OTHER"))

ABUSE_TYPE = (("PHYSICAL", "PHYSICAL"), ("MENTAL", "MENTAL"))


class CategoryModel(BaseModel):
    category_name = models.CharField(max_length=50)
    category_icon = models.ImageField(upload_to="category", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    def __str__(self):
        return self.category_name


class CaseModel(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=50, blank=True)
    id_card = models.ImageField(upload_to="id_card", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    media = models.FileField(upload_to="case_media", max_length=100, null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=50, null=True, blank=True)
    height = models.FloatField(null=True, blank=True, validators=[validate_severity])
    category = models.OneToOneField(CategoryModel, on_delete=models.CASCADE, default="1a95a597-1cb8-42c1-a18c-41d6ef84975b")
    latittude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    severity = models.FloatField(default=0, validators=[validate_severity])
    additional_info = models.TextField(null=True, blank=True)
    def get_age(self):
        try:
            today = date.today()
            age = today.year - self.dob.year
            return age
        except Exception as e:
            print(e)
    def __str__(self):
        return self.title
    class Meta:
        abstract = True


class OthersCaseModel(CaseModel):
    information = models.TextField(null=True, blank=True)

class AbuseCaseModel(CaseModel):
    who_is_abused = models.CharField(choices=PERSON_SELECTOR, max_length=50)
    abuse_type = models.CharField(choices=ABUSE_TYPE, max_length=50)
    injurured = models.BooleanField(default=False)
    injururies = models.TextField(null=True, blank=True)

class IntoxicationCaseModel(CaseModel):
    drug_or_alcohol_consumed = models.BooleanField(default=False)
    drug_or_alcohol_consumption = models.FloatField(null=True, blank=True, validators=[validate_alcoholic])
    troubling_others = models.BooleanField(default=False)

class AggresssionCaseModel(CaseModel):
    weapon_used = models.BooleanField(default=False)
    weapons_used = models.TextField(null=True, blank=True)
    injurured = models.BooleanField(default=False)
    injururies = models.TextField(null=True, blank=True)

class MotorIncidentCaseModel(CaseModel):
    others_property_damaged = models.BooleanField(default=False)
    indirect_or_perposefuly_damaged = models.BooleanField(default=False)

class ExploitationCaseModel(CaseModel):
    ragging = models.BooleanField(default=False)


class CaseImagesModel(BaseModel):
    case = models.ForeignKey(CaseModel, related_name="related_case_imgs", on_delete=models.CASCADE)
    img = models.ImageField(upload_to="case_img", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.case.title
    class Meta:
        abstract = True
