from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from core.settings import BASE_DIR

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


# @api_view(["POST"])
# def dashboardView(request):
#     try:
#         pass
#     except Exception as e:
#         return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(["POST"])
# def analyticsView(request):
#     try:
#         pass
#     except Exception as e:
#         return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddCases(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CaseModel.objects.all()
    serializer_class = CaseModelSerializer

class AddPerson(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PersonModel.objects.all()
    serializer_class = PersonModelSerializer
    def create(self, request):
        try:
            ser = PersonModelSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                obj = PersonModel.objects.get(id=ser.data["id"])
                path_of_img = "data/" + str(obj.id_card)
                im = Image.open(path_of_img)
                x = getDetails(im)
                if len(x) == 4:
                    obj.name = x[0]
                    obj.id_number = x[2]
                    obj.dob = x[1]
                    obj.gender = x[3]
                elif len(x) == 3:
                    obj.name = x[0]
                    obj.id_number = x[1]
                    obj.dob = x[2]
                obj.save()
                return Response({"message":"Person Added", "data":ser.data}, status=status.HTTP_200_OK)
            return Response({"error":str(ser.errors)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


class RescentCases(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CaseModel.objects.all().order_by("-created_at")
    serializer_class = CaseModelSerializer


@api_view(["POST"])
def searchCases(request):
    try:
        ser = SearchSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            if ser.data["img"] != NULL:
                img_path = str(BASE_DIR) + "/data/" + ser.data["img"]
                res = match_face(img_path)
                if res == False:
                    return  Response({"message":"Match Not Found"}, status=status.HTTP_404_NOT_FOUND)
                else :
                    res_img_path = str(BASE_DIR) + "/data/" + res
                    if not PersonModel.objects.filter(img=res_img_path):
                        return  Response({"message":"Match Not Found"}, status=status.HTTP_404_NOT_FOUND)
                    else:
                        obj = PersonModel.objects.get(img=res_img_path)
                        ret_ser = PersonModelSerializer(obj)
                        return Response({"message":"Match Found", "data":ret_ser.data}, status=status.HTTP_200_OK)
            if ser.data["text"] != None:
                search_string = ser.data["text"]
                if CaseModel.objects.filter(title__icontains=search_string, description__icontains=search_string, additional_info__icontains=search_string).exists():
                    objs = CaseModel.objects.filter(title__icontains=search_string, description__icontains=search_string, additional_info__icontains=search_string)
                    res_ser = CaseModelSerializer(objs, many=True)
                    return Response({"message":"Data Found", "data":res_ser.data}, status=status.HTTP_200_OK)
                else:
                    return Response({"message":"Data not found"}, status=status.HTTP_404_NOT_FOUND)
            if ser.data["longitude"] != None and ser.data["latitude"] != None:
                lat = ser.data["longitude"]
                lon = ser.data["latitude"]
                return Response({"message":"Data Found", "data":res_ser.data}, status=status.HTTP_200_OK)
        return Response({"error":str(ser.errors)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


