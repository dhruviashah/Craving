from django.db import models
from recipe.models import Recipe
from user_profile.models import UserProfile
import datetime

# Create your models here.
class Order(models.Model):
    
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    delivered = models.BooleanField(default=False)
    product = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    

    def placeOrder(self):
        self.save()
