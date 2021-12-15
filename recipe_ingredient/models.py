from django.db import models
from ingredient.models import Ingredient
from recipe.models import Recipe
from unit_of_measure.models import UnitOfMeasure

# Create your models here.

class RecipeIngredient(models.Model):
    '''
    Association table of recipe and Ingredient
    '''
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    choice = (
        ('gram','g'),
        ('kilogram','kg'),
        ('mililiter','ml'),
        ('liter','l'),
    )
    unit_converter = models.ForeignKey(UnitOfMeasure, on_delete = models.CASCADE, blank = True)


    def __str__(self):
        """
        Returns a string representation of this 'recipre-ingredient'.
        This string is used when a 'recipre-ingredient' is printed in the console.
        """
        return self.ingredient

