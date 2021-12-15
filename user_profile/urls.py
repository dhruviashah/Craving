from django.urls import path, include
from recipe import urls as recipeUrls
from .views import (
	UserProfileView,
	user_list,
	home_form,
	edit_profile)
from recipe.views import (recipe_list)

urlpatterns = [
   path('user-profile',UserProfileView.as_view(),name='user_add'),
   path('user-profile/<int:pk>',UserProfileView.as_view(),name='user_details'),
   path('user-profile-list',user_list,name='role_list'),
   # path('user-profile-register',user_profile_registration_form,name='registration 2'),
   path('home',home_form,name='home'),
   path('edit_profile',edit_profile,name='edit_profile'),
   path('user-profile/recipe-list/',recipe_list),
]	