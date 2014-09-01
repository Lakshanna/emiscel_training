from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import *

# Create your models here.
schoice = (('I','Std.I'),('II','Std.II'),('III','Std.III'),('IV','Std.IV'),('V', 'Std.V'))
tchoice = (('M', 'Male'),('F','Female'))
# #rchoice = (('Hindu','Hindu'),('Muslim','Muslim'),('Christian','Christian'),('Others','Others'))
# # cchoice = (('OC','Other Caste'),('BC','Backward caste'),('MBC','Most Backward Caste'),('SC','Scheduled Caste'))
# lchoice = (('Tamil','Tamil'),('English','English'),('Malayalam','Malayalam'),('Telugu','Telugu'),('Ohters','Ohters'))
# dchoice = (('Kanchipuram','Kanchipuram'),('Tiruvallur','Tiruvallur'),('Cuddalore','Cuddalore'),('Villupuram','Villupuram'),('Vellore','Vellore'),('Tiruvannamalai','Tiruvannamalai'),('Salem','Salem'),('Namakkal','Namakkal'),('Dharmapuri','Dharmapuri'),('Erode','Erode'),('Coimbatore','Coimbatore'),('The Nilgiris','The Nilgiris'),('Thanjavur','Thanjavur'),('Nagapattinam','Nagapattinam'),('Tiruvarur','Tiruvarur'),('Tiruchirappalli','Tiruchirappalli'),('Karur','Karur'),('Perambalur','Perambalur'),('Pudukkottai','Pudukkottai'),('Madurai','Madurai'),('Theni','Theni'),('Dindigul','Dindigul'),('Ramanathapuram','Ramanathapuram'),('Virudhunagar','Virudhunagar'),('Sivagangai','Sivagangai'),('Tirunelveli','Tirunelveli'),('Thoothukkudi','Thoothukkudi'),('Kanniyakumari','Kanniyakumari'),('Krishnagiri','Krishnagiri'),('Ariyalur','Ariyalur'),('Tiruppur','Tiruppur'))
# nchoice = (('Indian','Indian'),('Others','Others'))
# mchoice = (('Tamil','Tamil'),('English','English'),('Malayalam','Malayalam'),('Telugu','Telugu'),('Ohters','Ohters'))


class community(models.Model):
	id = models.AutoField(primary_key=True,)
	subcaste=models.CharField(max_length=25,default='BC',blank=True,)
	def __unicode__ (self):
		return self.subcaste



class religion(models.Model):
	id=models.AutoField(primary_key=True,)
	rel_name=models.CharField(max_length=20,default='Hindu',blank=True,)
	def __unicode__ (self):
		return self.rel_name

class language(models.Model):
	id=models.AutoField(primary_key=True,)
	lang_name=models.CharField(max_length=20,default='Tamil',blank=True,)
	def __unicode__ (self):
		return self.lang_name

class medium(models.Model):
	id=models.AutoField(primary_key=True,)
	medium_name=models.CharField(max_length=20,default='Tamil',blank=True,)
	def __unicode__ (self):
		return self.medium_name



class district(models.Model):
	id=models.AutoField(primary_key=True,)
	dist_name=models.CharField(max_length=20,default='Chennai',blank=True,)
	def __unicode__ (self):
		return self.dist_name


# class nationality(models.Model):
# 	id=models.AutoField(primary_key=True,)
# 	nat_name=models.CharField(max_length=20,default='Indian',blank=True,)
# 	def __unicode__ (self):
# 		return self.nat_name

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	company = models.CharField(max_length=255, blank=True,)
	website = models.URLField(blank=True,)
	def __unicode__ (self):
		return self.user.username


class stud_details(models.Model):
	Studid = models.AutoField(primary_key=True,)
	Name = models.CharField(max_length=255,)
	Std = models.CharField(max_length=4,choices=schoice,default='I',)
	Sex = models.CharField(max_length=1,choices=tchoice,default='M',)
	Dob = models.DateField()
	Medium = models.ForeignKey(medium)
	# Nationality = models.ForeignKey(nationality)
	Mother_tongue=models.ForeignKey(language)
	Community=models.ForeignKey(community)
	Religion=models.ForeignKey(religion)
	District=models.ForeignKey(district)
	Phone_no=models.IntegerField()
	Address=models.CharField(max_length=50,)
	Pin_code=models.IntegerField()
	
	def __unicode__ (self):
   		return ' '.join([self.Name])