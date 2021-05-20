from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
	first_name = models.CharField(max_length=100, null=False, blank=False)
	last_name = models.CharField(max_length=100, null=False, blank=False)
	email = models.EmailField(null=False, blank=False)
	phone = models.CharField(max_length=50,null=False, blank=False)
	date_of_birth = models.DateField(null=False, blank=False)
	user = models.OneToOneField(User, on_delete = models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.first_name + " " + self.last_name