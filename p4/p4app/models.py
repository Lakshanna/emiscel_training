from django.db import models
from django.db.models.fields import *
from django.contrib.auth.models import User


class Classstudying(models.Model):
	id = models.AutoField(primary_key=True)
	standard = models.CharField(max_length=10)
	def __str__(self):
		return self.standard

class Student(models.Model):
	id = models.AutoField(primary_key=True)
	sid = models.IntegerField()
	name = models.CharField(max_length=50)
	father_name= models.CharField(max_length=50)
	school = models.CharField(max_length=100)
	std= models.ForeignKey(Classstudying)
	tamil = models.IntegerField()
	english = models.IntegerField()
	maths = models.IntegerField()
	science = models.IntegerField()
	social = models.IntegerField()
	total = models.IntegerField()

	def __str__(self):
		return self.std

class Userprofile(models.Model):
	user = models.OneToOneField(User)
	school = models.CharField(max_length= 100,blank = True)
	district = models.CharField(max_length = 100,blank = True)

# Create your models here.
