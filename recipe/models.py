from django.db import models

# Create your models here.
class Recipe(models.Model):
	recipe_name = models.TextField(blank=False)
	img = models.ImageField(blank=True)
	cooking_serving = models.IntegerField(blank=False)
	cooking_time = models.TextField(blank=False)
	recipe_price = models.IntegerField(blank=True, default=0)
	category = models.IntegerField(blank=True, default=1)
	

	# @property
	# def recipe_price(self):
	# 	return self._recipe_price
	
