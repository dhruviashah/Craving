"""
user urls
"""
from django.urls import path, include
from user_profile import urls as ProfileUrls
from recipe import urls as recipeUrls
from .views import (
	users,
	user_list,
	user_form,
	registration_form,
    customer_login,
    admin_form,
    logout,
    delivery_dashboard,
    staff_dashboard)
from .views import obtain_auth_token  # <-- Here


urlpatterns = [
    path('user',users.as_view(),name='user_add'),
    path('user/<int:pk>',users.as_view(),name='user_details'),
    path('user_list',user_list,name='user_list'),
    path('user_form',user_form,name='user_form'),
    path('register',registration_form,name='register'),
    path('login', obtain_auth_token, name='api_token_auth'),
    # path('login', customer_login, name='api_token_auth'),
    path('admin_form',admin_form,name='admin_page'),
    path('logout',logout,name='logout'),
    path('delivery_dashboard',delivery_dashboard,name='delivery_dashboard'),
    path('staff_dashboard',staff_dashboard,name='staff_dashboard'),
    path('',include(ProfileUrls)),
    ]

