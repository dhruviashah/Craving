from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class BaseModel(AbstractBaseUser):
	created_date = models.DateTimeField(default=datetime.now(), blank=False)
	modfied_date = models.DateTimeField(default=datetime.now(), blank=True)

	class Meta:
		abstract = True