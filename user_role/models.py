from django.db import models
from base.models import BaseModel

# Create your models here.
class UserRole(BaseModel):
	role_name = models.CharField(max_length=20)