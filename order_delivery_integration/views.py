from django.shortcuts import render
from django.shortcuts import render, redirect
from .serializers import OrderDeliveryJoinSerializer
from .models import OrderDeliveryJoin

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser

# Create your views here.
class OrderDeliveryJoinView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request):

        delivery_person = None
        user = None

        if 'delivery_person' in request.POST:
            delivery_person = request.POST.get('delivery_person')
        if 'user' in request.POST:
            user = request.POST.get('user')

        data = {'delivery_person':delivery_person,
                'user':user}

        serializer = OrderDeliveryJoinSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("wait+++++")
