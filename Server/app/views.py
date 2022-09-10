from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from authentication.models import PoliceModel
from .serializers import *
from .models import *


class GetCategories(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerialzer

class AddCategories(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerialzer

class CategoriesRUD(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerialzer
    lookup_field = "id"


