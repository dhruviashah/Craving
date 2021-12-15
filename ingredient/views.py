from django.shortcuts import render
from .models import Ingredient
from .serializers import IngredientSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.decorators import api_view
# Create your views here.

class IngredientView(APIView):

	def post(self, request):
		data = JSONParser().parse(request)
		if not data:
			return JsonResponse({'message':'Data not provided'}, status=status.HTTP_204_NO_CONTENT)
		serializer = IngredientSerializer(data= data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status = status.HTTP_200_OK)
		return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk):
		try:
			ingredient = Ingredient.objects.get(pk = pk)
		except ingredient.DoesNotExist:
			return JsonResponse({'message': 'ingredient not exist'}, status=status.HTTP_404_NOT_FOUND)
		ingredient_data = JSONParser().parse(request)
		ingredient_serializer = IngredientSerializer(ingredient, data = ingredient_data)
		if ingredient_serializer.is_valid():
			ingredient_serializer.save()
			return JsonResponse(ingredient_serializer.data,status = status.HTTP_200_OK)
		return JsonResponse(ingredient_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def get(self, request, pk):
		try:
			ingredient = Ingredient.objects.get(pk = pk)
		except ingredient.DoesNotExist:
			return JsonResponse({'message': 'ingredient not exist'}, status=status.HTTP_404_NOT_FOUND)
		ingredient_serializer = IngredientSerializer(ingredient)
		return JsonResponse(ingredient_serializer.data)

	def delete(self, request, pk):
		try:
			ingredient = Ingredient.objects.get(pk = pk)
		except ingredient.DoesNotExist:
			return JsonResponse({'message': 'ingredient not exist'}, status=status.HTTP_404_NOT_FOUND)
		ingredient.delete()
		return JsonResponse({'message': 'ingredient was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def ingredient_list(request):
	ingredient_data = Ingredient.objects.all()
	ingredient_serializer = IngredientSerializer(ingredient_data, many = True)
	# return JsonResponse(ingredient_serializer.data, safe = False)
	return render(request,'ingredient/Add_product_2.html',{'ingredient':ingredient_data})

