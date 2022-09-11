from statistics import mode
from rest_framework import serializers
from .models import *


class CategoryModelSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["id", "category_name", "category_icon"]


class CaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseModel
        fields = "__all__"


class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel
        fields = "__all__"