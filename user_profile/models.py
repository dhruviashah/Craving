from django.db import models
from base.models import BaseModel
from user_role.models import UserRole
from user.models import User

# Create your models here.
class UserProfile(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	address = models.CharField(max_length=50)
	contact_number = models.IntegerField(max_length=10)
	role_id = models.ForeignKey(UserRole, on_delete=models.CASCADE, default=2)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)

	# USERNAME_FIELD = User.email