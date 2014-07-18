from django.db import models
from django.db.models.fields import *


class student_details(models.Model):
	uid = models.IntegerField()
	name = models.CharField(max_length=50)
	gender = models.CharField(max_length=15)
	mother_tongue = models.CharField(max_length=20)	
	nationality = models.CharField(max_length=20)