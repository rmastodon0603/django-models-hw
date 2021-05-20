from django.db import models
from teachers.models import Teacher

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False)
	description = models.TextField()
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	start = models.DateField(null=True)
	end = models.DateField(null=True)

	def __str__(self):
		return self.name