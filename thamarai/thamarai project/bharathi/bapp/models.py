from django.db import models
from django.db.models.fields import *
from django.contrib.auth.models import User
# Create your models here.


class studying(models.Model):
	id = models.AutoField(primary_key = True)
	standard = models.IntegerField()

	# def __str__(self):
 #  		return self.standard



class student(models.Model):
	id = models.AutoField(primary_key = True)
	uid = models.IntegerField()
	name = models.CharField(max_length=50)
	fname = models.CharField(max_length=50)
	school = models.CharField(max_length=50)
	std = models.ForeignKey(studying)
	tam = models.IntegerField()
	eng = models.IntegerField()
	mat = models.IntegerField()
	phy = models.IntegerField()
	chem = models.IntegerField()
	bio = models.IntegerField()
	tot = models.IntegerField()
	
	# def __str__(self):
 #  		return self.std




class Userprofile(models.Model):
  	user=models.OneToOneField(User)
  	company=models.CharField(max_length=50,blank=True)
  	website=models.URLField(max_length=50,blank=True)


  	def __unicode__(self):
  		return self.user.username


