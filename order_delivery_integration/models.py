from django.db import models
from order.models import Order
from user.models import User
from order_delivery.models import OrderDelivery
from user_profile.models import UserProfile 

# Create your models here.
class OrderDeliveryJoin(models.Model):
	delivery_person = models.ForeignKey(OrderDelivery, on_delete=models.CASCADE)
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)