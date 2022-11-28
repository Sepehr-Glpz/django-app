from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import EntryRequestSerializer, ManagementUserSerializer
from entry.models import EntryRequest
from management.models import ManagementUser
from django.http import JsonResponse
from .models import ApiResponse, serialize_users
from entry.views import create_invite_link

# Create your views here.


class EntryRequestView(APIView):
    def post(self, request):
        serializer = EntryRequestSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            data = {"link": create_invite_link(instance.id, request)}
            response = ApiResponse(True, [], data)
            return JsonResponse(response.__dict__)
        else:
            response = ApiResponse(False, ["Error"], None)
            return JsonResponse(response.__dict__)

class ManagmentUserView(APIView):
    def get(self, request):
        try:
            users_models = ManagementUser.objects.all()
            serializer = ManagementUserSerializer(data=users_models, many=True)
            serializer.is_valid()
            response = ApiResponse(True, [], serializer.data)
            return JsonResponse(response.__dict__)
        except:
            response = ApiResponse(False, ["An Error occurred"], None)
            return JsonResponse(response.__dict__)