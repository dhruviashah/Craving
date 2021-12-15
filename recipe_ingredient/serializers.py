from rest_framework import serializers
from .models import UnitOfMeasure, RecipeIngredient

class UnitOfMeasureSerializer(serializers.ModelSerializer):
	class Meta:
		model = UnitOfMeasure
		fields = '__all__'


class RecipeIngredientSerialaizer(serializers.ModelSerializer):
	class Meta:
		model = RecipeIngredient
		fields = '__all__'