from rest_framework import serializers
from .models import *


class loginSerializer(serializers.Serializer):
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True)


class signupSerializer(serializers.Serializer):
    f_name = serializers.CharField(required = True)
    l_name = serializers.CharField(required = True)
    email = serializers.EmailField(required = True)
    phone = serializers.CharField(required = False)
    password = serializers.CharField(required = True)


class otpSerializer(serializers.Serializer):
    otp = serializers.IntegerField(required = True)
    pw = serializers.CharField(required = False)


class emailSerializer(serializers.Serializer):
    email = serializers.EmailField(required = True)


class AddPoliceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddPoliceModel
        fields = ["file"]


class AddPoliceAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddPoliceAdminModel
        fields = ["file"]

class AddIndividualPoliceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceModel
        fields = ["f_name", "l_name", "rank", "phone", "email", "profile_img"]

class SpecialEmailSerializer(serializers.Serializer):
    sub = serializers.CharField(required = True)
    body = serializers.CharField(required = True)
