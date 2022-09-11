from rest_framework import serializers
from .models import *

class CategoryModelSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["id", "category_name", "category_icon"]


class OthersCaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OthersCaseModel
        fields = "__all__"
class AbuseCaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbuseCaseModel
        fields = "__all__"
class IntoxicationCaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntoxicationCaseModel
        fields = "__all__"
class AggresssionCaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggresssionCaseModel
        fields = "__all__"
class MotorIncidentCaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotorIncidentCaseModel
        fields = "__all__"
class ExploitationCaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExploitationCaseModel
        fields = "__all__"