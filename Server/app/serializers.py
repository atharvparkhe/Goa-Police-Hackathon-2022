from rest_framework import serializers
from .models import *

class CategoryModelSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["id", "category_name", "category_icon"]