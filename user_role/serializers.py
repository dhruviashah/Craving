from rest_framework import serializers

from .models import UserRole

class UserRoleSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserRole
		fields = ['role_name']
		