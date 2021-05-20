from django.db import models
from cources.models import Course

# Create your models here.
class Student(models.Model):
	first_name = models.CharField(max_length=100, null=False, blank=False)
	last_name = models.CharField(max_length=100, null=False, blank=False)
	email = models.EmailField()
	phone = models.CharField(max_length=50)
	facebook = models.URLField(null=True)
	date_of_birth = models.DateField()
	cources = models.ManyToManyField(Course)

	def __str__(self):
		return self.first_name + " " + self.last_name