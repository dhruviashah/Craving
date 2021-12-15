from rest_framework import serializers
from .models import OrderDeliveryJoin

class OrderDeliveryJoinSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderDeliveryJoin
		fields = '__all__'