from django.db import models
from base.models import BaseModel
from .validators import *
from .utils import *


GENDER = (("MALE", "MALE"), ("FEMALE", "FEMALE"), ("OTHERS", "OTHERS"))

PERSON_SELECTOR = (("MEN", "MEN"), ("WOMEN", "WOMEN"), ("CHILD", "CHILD"), ("OTHER", "OTHER"))

ABUSE_TYPE = (("PHYSICAL", "PHYSICAL"), ("MENTAL", "MENTAL"))

VICTIM = (("MINOR", "MINOR"), ("FEMALE", "FEMALE"), ("CHILD", "CHILD"), ("OTHER", "OTHER"))



class CategoryModel(BaseModel):
    category_name = models.CharField(max_length=50)
    category_icon = models.ImageField(upload_to="category", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    def __str__(self):
        return self.category_name


class CaseModel(BaseModel):
    title = models.CharField(max_length=50)
    category = models.OneToOneField(CategoryModel, on_delete=models.CASCADE)
    severity = models.FloatField(default=0, validators=[validate_severity])
    description = models.TextField(null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to="case_img", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    media = models.FileField(upload_to="case_media", max_length=100, null=True, blank=True)
    latittude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    who_is_abused = models.CharField(null=True, blank=True, choices=PERSON_SELECTOR, max_length=50)
    abuse_type = models.CharField(null=True, blank=True, choices=ABUSE_TYPE, max_length=50)
    injurured = models.BooleanField(default=False)
    injururies = models.TextField(null=True, blank=True)
    drugs = models.BooleanField(default=False)
    alcohol = models.BooleanField(default=False)
    consumption_level = models.FloatField(null=True, blank=True, validators=[validate_alcoholic])
    intoxicant = models.TextField(null=True, blank=True)
    troubling_others = models.BooleanField(default=False)
    weapon_used = models.BooleanField(default=False)
    weapons_used = models.TextField(null=True, blank=True)
    others_property_damaged = models.BooleanField(default=False)
    perposefuly_damaged = models.BooleanField(default=False)
    victim = models.CharField(null=True, blank=True, choices=VICTIM, max_length=50)
    def __str__(self):
        return self.title


class PersonModel(BaseModel):
    name = models.CharField(max_length=50, blank=True)
    id_number = models.CharField(null=True, blank=True, max_length=20)
    id_card = models.ImageField(upload_to="id_card", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    dob = models.CharField( max_length=20, null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=50, null=True, blank=True)
    img = models.ImageField(upload_to="user_img", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    height = models.FloatField(null=True, blank=True, validators=[validate_severity])
    case = models.ForeignKey(CaseModel, related_name="case_suspects", on_delete=models.CASCADE)
    # def get_age(self):
    #     try:
    #         today = date.today()
    #         age = today.year - self.dob.year
    #         return age
    #     except Exception as e:
    #         print(e)
    # def __str__(self):
    #     return self.name
    

class CaseImagesModel(BaseModel):
    case = models.ForeignKey(CaseModel, related_name="related_case_imgs", on_delete=models.CASCADE)
    img = models.ImageField(upload_to="case_img", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.case.title
