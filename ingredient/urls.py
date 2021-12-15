from django.urls import path
from .views import (
	IngredientView,
	ingredient_list)

urlpatterns = [
   path('ingredient/',IngredientView.as_view(),name='ingredient_add'),
   path('ingredient/<int:pk>',IngredientView.as_view(),name='ingredient_details'),
   path('ingredient-list/',ingredient_list,name='ingredient_list'),
]