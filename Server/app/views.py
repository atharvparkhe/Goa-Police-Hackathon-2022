from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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


@api_view(["POST"])
def dashboardView(request):
    try:
        pass
    except Exception as e:
            return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def analyticsView(request):
    try:
        pass
    except Exception as e:
            return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CasesLC(ListCreateAPIView):
    queryset = CaseModel.objects.all()
    serializer_class = CaseModelSerializer
