from django.db import models
from user.models import User

# Create your models here.
class OrderDelivery(models.Model):
    """docstring for OrderDelivery"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=10)
    status = models.BooleanField(default=True)
