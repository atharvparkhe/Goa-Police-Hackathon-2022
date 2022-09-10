from datetime import date
from django.db import models
from base.models import BaseModel
from .validators import *

GENDER = (("MALE", "MALE"), ("FEMALE", "FEMALE"), ("OTHERS", "OTHERS"))

class CategoryModel(BaseModel):
    category_name = models.CharField(max_length=50)
    category_icon = models.ImageField(upload_to="category", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    def __str__(self):
        return self.category_name


class GeneralCaseModel(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=50, blank=True)
    id_card = models.ImageField(upload_to="id_card", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    media = models.FileField(upload_to="case_media", max_length=100, null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=50, null=True, blank=True)
    height = models.FloatField(null=True, blank=True, validators=[validate_severity])
    category = models.ForeignKey(CategoryModel, related_name="related_category_cases", on_delete=models.CASCADE)
    latittude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    severity = models.FloatField(default=0, validators=[validate_severity])
    def get_age(self):
        try:
            today = date.today()
            age = today.year - self.dob.year
            return age
        except Exception as e:
            print(e)
    def __str__(self):
        return self.title
    


class CaseImagesModel(BaseModel):
    case = models.ForeignKey(GeneralCaseModel, related_name="related_case_imgs", on_delete=models.CASCADE)
    img = models.ImageField(upload_to="case_img", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.case.title
    

