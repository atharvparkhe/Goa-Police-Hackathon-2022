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


class OthersCasesLC(ListCreateAPIView):
    queryset = OthersCaseModel.objects.all()
    serializer_class = OthersCaseModelSerializer
class AbuseCasesLC(ListCreateAPIView):
    queryset = AbuseCaseModel.objects.all()
    serializer_class = AbuseCaseModelSerializer
class IntoxicationCaseLC(ListCreateAPIView):
    queryset = IntoxicationCaseModel.objects.all()
    serializer_class = IntoxicationCaseModelSerializer
class AggresssionCaseLC(ListCreateAPIView):
    queryset = AggresssionCaseModel.objects.all()
    serializer_class = AggresssionCaseModelSerializer
class MotorIncidentCaseLC(ListCreateAPIView):
    queryset = MotorIncidentCaseModel.objects.all()
    serializer_class = MotorIncidentCaseModelSerializer
class ExploitationCaseLC(ListCreateAPIView):
    queryset = ExploitationCaseModel.objects.all()
    serializer_class = ExploitationCaseModelSerializer