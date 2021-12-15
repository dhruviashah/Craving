from django.shortcuts import render
from .models import UserRole
from .serializers import UserRoleSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.decorators import api_view
# Create your views here.

class UserRoleView(APIView):

    def post(self, request):
        role_data = JSONParser().parse(request)
        if not role_data:
            return JsonResponse({'message':'Data not provided'}, status=status.HTTP_204_NO_CONTENT)
        role_serializer = UserRoleSerializer(data=role_data)
        if role_serializer.is_valid():
            role_serializer.save()
            return JsonResponse(role_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(role_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            role = UserRole.objects.get(pk=pk)
        except role.DoesNotExist:
            return JsonResponse({'message': 'The role does not exist'}, status=status.HTTP_404_NOT_FOUND)
        role_data = JSONParser().parse(request)
        role_serializer = UserRoleSerializer(role,data=role_data)
        if role_serializer.is_valid():
            role_serializer.save()
            return JsonResponse(role_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(role_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        try:
            role = UserRole.objects.get(pk=pk)
        except role.DoesNotExist:
            return JsonResponse({'message': 'The role does not exist'}, status=status.HTTP_404_NOT_FOUND)

        role_serializer = UserRoleSerializer(role)
        return JsonResponse(role_serializer.data)

    def delete(self, request, pk):
        try:
            role = UserRole.objects.get(pk=pk)
        except role.DoesNotExist:
            return JsonResponse({'message': 'The role does not exist'}, status=status.HTTP_404_NOT_FOUND)

        role.delete()
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def role_list(request):
    role_data = UserRole.objects.all()
    role_serializer = UserRoleSerializer(role_data, many=True)
    return JsonResponse(role_serializer.data, safe=False)
