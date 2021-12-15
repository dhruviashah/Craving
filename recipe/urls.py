from django.urls import path, include
from user_profile import urls as UserProfileUrls
from .views import (
	RecipeView,
	recipe_list,
	price_cal,
	product_list,
	add_product,
	edit_product,
	update,
   cart,
   cart_display,
   breakfast_recipe_list)

urlpatterns = [
   path('recipe',RecipeView.as_view(),name='recipe_add'),
   path('recipe/<int:pk>',RecipeView.as_view(),name='recipe_details'),
   path('recipe_list',recipe_list,name='recipe_list'),
   path('breakfast_recipe_list',breakfast_recipe_list,name='breakfast_recipe_list'),
   path('price-update/<int:pk>',price_cal, name='price_calculate'),
   path('product-list',product_list,name='view_product'),
   path('add_product',add_product,name='add_product'),
   path('edit_product/<int:pk>',edit_product,name='edit_product'),
   path('update/<int:pk>',update,name='update_product'),
   path('user_cart',cart,name='cart'),
   path('cart_display',cart_display,name='cart_item_display'),
]