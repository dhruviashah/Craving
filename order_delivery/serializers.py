from rest_framework import serializers
from .models import OrderDelivery

class OrderDeliverySerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderDelivery
		fields = '__all__'