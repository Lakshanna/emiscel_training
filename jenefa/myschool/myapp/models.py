from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import *


class sdetails(models.Model):
	sid=models.AutoField(primary_key=True,)
	sname=models.CharField(max_length=25,)
	sex=models.CharField(max_length=5,)
	std=models.CharField(max_length=5,)
	school=models.CharField(max_length=50,)

	def __unicode__(self):
		return self.sname


