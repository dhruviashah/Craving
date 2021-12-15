from django.urls import path
from .views import (
	RecipeIngredientView,
	all_list)

urlpatterns = [
   path('recipe-ingredient/',RecipeIngredientView.as_view(),name='ingredient_add'),
   path('recipe-ingredient/<int:pk>',RecipeIngredientView.as_view(),name='ingredient_details'),
   path('recipe-ingredient-list/',all_list,name='ingredient_list'),
]