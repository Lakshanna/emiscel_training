from django.db import models
from django.contrib.auth.models import User

# Create your models here.
tchoice = (('M', 'Male'),('F','Female'))
schoice = (('I','Std.I'),('II','Std.II'),('III','Std.III'),
	       ('IV','Std.IV'),('V', 'Std.V'))
class student(models.Model):
	studid = models.CharField(primary_key=True, max_length=12)
	name = models.CharField(max_length=255,)
	fname = models.CharField(max_length=255,)
	age = models.IntegerField()
	std = models.CharField(max_length=4,choices=schoice,default='I')
	sex = models.CharField(max_length=1,choices=tchoice, default='M')
	splchi = models.BooleanField(default=False,)
	photo = models.FileField(upload_to='photos')
	phys = models.IntegerField()
	chem = models.IntegerField()
	math = models.IntegerField()
	lang = models.IntegerField()
	total = models.IntegerField()
	email = models.EmailField()
	def __unicode__ (self):
	    return ' '.join([self.name, self.fname])

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	company = models.CharField(max_length=255, blank=True,)
	website = models.URLField(blank=True,)
	def __unicode__ (self):
		return self.user.username





