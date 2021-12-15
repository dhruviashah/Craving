from rest_framework import serializers
from .models import Recipe
from ingredient.models import Ingredient
from recipe_ingredient.models import RecipeIngredient

class RecipeSerializer(serializers.ModelSerializer):

	# recipe_price = serializers.SerializerMethodField(method_name='calculate_price')

	class Meta:
		model = Recipe
		fields = '__all__'


	
