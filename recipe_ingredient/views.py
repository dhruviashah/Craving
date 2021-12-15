from django.shortcuts import render
from .serializers import RecipeIngredientSerialaizer, UnitOfMeasureSerializer
from .models import RecipeIngredient

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.decorators import api_view
# Create your views here.

class RecipeIngredientView(APIView):

	def post(self, request):
		data = JSONParser().parse(request)
		if not data:
			return JsonResponse({'message':'data not provided'}, status = status.HTTP_204_NO_CONTENT)
		serializer = RecipeIngredientSerialaizer(data = data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status = status.HTTP_200_OK)
		return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def put(slef, request, pk):
		try:
			recipe_ingredient = RecipeIngredient.objects.get(pk = pk)
		except:
			return JsonResponse({'message':'data that you are looking for does not exist'}, status=status.HTTP_404_NOT_FOUND)
		data = JSONParser().parse(request)
		serializer = RecipeIngredientSerialaizer(recipe_ingredient, data= data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status = status.HTTP_200_OK)
		return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def get(self, request, pk):
		try:
			recipe_ingredient = RecipeIngredient.objects.get(pk = pk)
		except:
			return JsonResponse({'message':'data that you are looking for does not exist'}, status=status.HTTP_404_NOT_FOUND)
		serializer = RecipeIngredientSerialaizer(recipe_ingredient)
		return JsonResponse(serializer.data)

	def delete(self, request, pk):
		try:
			recipe_ingredient = RecipeIngredient.objects.get(pk = pk)
		except:
			return JsonResponse({'message':'data that you are looking for does not exist'}, status=status.HTTP_404_NOT_FOUND)
		recipe_ingredient.delete()
		return JsonResponse({'message': 'was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def all_list(request):
	data = RecipeIngredient.objects.all()
	serializer = RecipeIngredientSerialaizer(data, many=True)
	return JsonResponse(serializer.data, safe=False)



