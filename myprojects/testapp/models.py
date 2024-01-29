from django.db import models

# Create your models here.
class Employee(models.Model):
	name = models.CharField(max_length=200,blank=True)
	age = models.IntegerField(blank=True, null=True)
	position = models.CharField(max_length=200,blank=True)
	def __str__(self):
		return self.name + '  '+str(self.age)