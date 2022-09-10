from distutils import text_file
from distutils.text_file import TextFile
from django.db import models
from base.models import BaseModel


class GeneralCaseModel(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to="case_media", max_length=100, null=True, blank=True)
    latittude = models.FloatField()
    longitude = models.FloatField()
    location = models.CharField(max_length=50, null=True, blank=True)


class CaseImagesModel(BaseModel):
    case = models.ForeignKey(GeneralCaseModel, related_name="related_case_imgs", on_delete=models.CASCADE)
    img = models.ImageField(upload_to="case_img", height_field=None, width_field=None, max_length=None)


