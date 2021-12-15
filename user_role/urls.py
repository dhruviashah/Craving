from django.urls import path
from .views import (
	UserRoleView,
	role_list)

urlpatterns = [
   path('role/',UserRoleView.as_view(),name='role_add'),
   path('role/<int:pk>',UserRoleView.as_view(),name='user_details'),
   path('role-list/',role_list,name='role_list'),
]