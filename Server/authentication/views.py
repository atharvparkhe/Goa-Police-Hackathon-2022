from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .threads import *
from .models import *
from .utils import *
import xlrd

from django.contrib.auth.hashers import make_password


@api_view(["POST"])
def addPoliceOfficers(request):
    try:
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAdminUser]
        ser = AddPoliceSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            file = ser.data["file"]
            path = str(settings.BASE_DIR)+str(file)
            workbook = xlrd.open_workbook(path)
            sheet = workbook.sheet_by_index(0)
            for row in range(1,sheet.nrows):
                org = PoliceModel.objects.create(
                    f_name = str(sheet.cell_value(row,0)).capitalize(),
                    l_name = str(sheet.cell_value(row,1)).capitalize(),
                    email = str(sheet.cell_value(row,2)).lower(),
                    phone = sheet.cell_value(row,3),
                    rank = sheet.cell_value(row,4)
                    )
                pw = get_random_string(8)
                org.set_password(pw)
                thread_obj = send_police_mail(str(sheet.cell_value(row,2)).lower(), pw)
                thread_obj.start()
                org.save()
            return Response({"message":"Police Officers Added"}, status=status.HTTP_201_CREATED)
        return Response({"error":ser.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def addPoliceAdminOfficers(request):
    try:
        ser = AddPoliceAdminSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            file = ser.data["file"]
            path = str(settings.BASE_DIR)+str(file)
            workbook = xlrd.open_workbook(path)
            sheet = workbook.sheet_by_index(0)
            for row in range(1,sheet.nrows):
                org = PoliceHeadModel.objects.create(
                    f_name = str(sheet.cell_value(row,0)).capitalize(),
                    l_name = str(sheet.cell_value(row,1)).capitalize(),
                    email = str(sheet.cell_value(row,2)).lower(),
                    phone = sheet.cell_value(row,3),
                    rank = sheet.cell_value(row,4)
                    )
                pw = get_random_string(8)
                org.set_password(pw)
                thread_obj = send_police_mail(str(sheet.cell_value(row,2)).lower(), pw)
                thread_obj.start()
                org.save()
            return Response({"message":"Police Admin Officers Added"}, status=status.HTTP_201_CREATED)
        return Response({"error":ser.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def addPoliceIndivisualOfficer(request):
    try:
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAdminUser]
        ser = AddIndividualPoliceSerializer(data=request.data)
        if ser.is_valid():
            pw = get_random_string(8)
            thread_obj = send_police_mail(str(ser.validated_data["email"]).lower(), pw)
            thread_obj.start()
            ser.save(password=make_password(pw))
            return Response({"message":"Police Officer Added"}, status=status.HTTP_201_CREATED)
        return Response({"error":ser.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def login(request):
    try:
        data = request.data
        serializer = loginSerializer(data=data)
        if serializer.is_valid():
            email = serializer.data["email"]
            password = serializer.data["password"]
            customer_obj = PoliceModel.objects.filter(email=email).first()
            if customer_obj is None:
                return Response({"message":"Account does not exist"}, status=status.HTTP_404_NOT_FOUND)
            user = authenticate(email=email, password=password)
            if not user:
                return Response({"message":"Incorrect password"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            jwt_token = RefreshToken.for_user(user)
            return Response({"message":"Login successfull", "token":str(jwt_token.access_token)}, status=status.HTTP_202_ACCEPTED)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def forgot(request):
    try:
        data = request.data
        serializer = emailSerializer(data=data)
        if serializer.is_valid():
            email = serializer.data["email"]
            user_obj = PoliceModel.objects.filter(email=email).first()
            if not user_obj:
                return Response({"message":"User does not exist."}, status=status.HTTP_404_NOT_FOUND)
            thread_obj = send_forgot_otp(email)
            thread_obj.start()
            return Response({"message":"reset mail sent"}, status=status.HTTP_200_OK)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EditOfficerProfile(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = PoliceModel.objects.all()
    serializer_class = PoliceProfileSerializer
    lookup_field = "id"


@api_view(["POST"])
def reset(request):
    try:
        data = request.data
        serializer = otpSerializer(data=data)
        if serializer.is_valid():
            otp = serializer.data["otp"]
            if not cache.get(otp):
                return Response({"message":"OTP expired"}, status=status.HTTP_408_REQUEST_TIMEOUT)
            if not PoliceModel.objects.filter(email=cache.get(otp)).first():
                return Response({"message":"user does not exist"}, status=status.HTTP_404_NOT_FOUND)
            user_obj = PoliceModel.objects.get(email=cache.get(otp))
            pw = serializer.data["pw"]
            user_obj.set_password(pw)
            user_obj.save()
            return Response({"message":"Password changed successfull"}, status=status.HTTP_202_ACCEPTED)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def specialEmail(request):
    try:
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAdminUser]
        email_recieptants = list(PoliceModel.objects.all().values_list("email", flat=True))
        if not email_recieptants:
            return Response({"message":"No Email Reciepttants"}, status=status.HTTP_403_FORBIDDEN)
        ser = SpecialEmailSerializer(data=request.data)
        if ser.is_valid():
            thread_obj = send_special_email(ser.data["sub"], ser.data["body"], email_recieptants)
            thread_obj.start()
            return Response({"message":"Email Sent"}, status=status.HTTP_200_OK)
        return Response({"error":ser.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def admin_login(request):
    try:
        data = request.data
        serializer = loginSerializer(data=data)
        if serializer.is_valid():
            email = serializer.data["email"]
            password = serializer.data["password"]
            customer_obj = PoliceHeadModel.objects.filter(email=email).first()
            if customer_obj is None:
                return Response({"message":"Account does not exist"}, status=status.HTTP_404_NOT_FOUND)
            user = authenticate(email=email, password=password)
            if not user:
                return Response({"message":"Incorrect password"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            jwt_token = RefreshToken.for_user(user)
            return Response({"message":"Login successfull", "token":str(jwt_token.access_token)}, status=status.HTTP_202_ACCEPTED)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def admin_forgot(request):
    try:
        data = request.data
        serializer = emailSerializer(data=data)
        if serializer.is_valid():
            email = serializer.data["email"]
            user_obj = PoliceHeadModel.objects.filter(email=email).first()
            if not user_obj:
                return Response({"message":"User does not exist."}, status=status.HTTP_404_NOT_FOUND)
            thread_obj = send_forgot_otp(email)
            thread_obj.start()
            return Response({"message":"reset mail sent"}, status=status.HTTP_200_OK)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def admin_reset(request):
    try:
        data = request.data
        serializer = otpSerializer(data=data)
        if serializer.is_valid():
            otp = serializer.data["otp"]
            if not cache.get(otp):
                return Response({"message":"OTP expired"}, status=status.HTTP_408_REQUEST_TIMEOUT)
            if not PoliceHeadModel.objects.filter(email=cache.get(otp)).first():
                return Response({"message":"user does not exist"}, status=status.HTTP_404_NOT_FOUND)
            user_obj = PoliceHeadModel.objects.get(email=cache.get(otp))
            pw = serializer.data["pw"]
            user_obj.set_password(pw)
            user_obj.save()
            return Response({"message":"Password changed successfull"}, status=status.HTTP_202_ACCEPTED)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
