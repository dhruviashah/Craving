from django.shortcuts import render
from .models import OrderDelivery
from .serializers import OrderDeliverySerializer

from order.models import Order
from order.serializers import OrderSerializer
from recipe.models import Recipe
from user_profile.models import UserProfile
from user_profile.serializers import UserProfileSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

