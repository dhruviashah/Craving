from django.db import models
from unit_of_measure.models import UnitOfMeasure
#from recipe_ingredient.models import UnitOfMeasure

# Create your models here.
class Ingredient(models.Model):
	name = models.CharField(max_length=30)
	price = models.IntegerField()
	choice = (
		('gram','g'),
		('kilogram','kg'),
		('mililiter','ml'),
		('liter','l'),
	)
	unit_converter = models.ForeignKey(UnitOfMeasure, on_delete = models.CASCADE, blank = True)