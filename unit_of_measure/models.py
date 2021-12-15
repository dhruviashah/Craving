from django.db import models

# Create your models here.
class UnitOfMeasure(models.Model):
    '''
    model for uom 
    '''
    name = models.CharField(max_length=10, blank=False)
    conversion_based = models.CharField(max_length=10, blank=True)
    conversion = models.IntegerField()

    def __str__(self):
        """
        Returns a string representation of this 'unitofmeasure'.
        This string is used when a 'unitofmeasure' is printed in the console.
        """
        return self.name