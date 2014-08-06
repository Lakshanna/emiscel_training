from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Signup(models.Model):

	user=models.OneToOneField(User)          
	company=models.CharField(max_length=255,blank=True)
	website=models.URLField(blank=True)
	name = models.CharField(max_length=255)



class Student(models.Model):
	MALE = 'Male'
	FEMALE = 'Female'
	

	SEX_CHOICES = (
	(MALE, 'Male'),
	(FEMALE, 'Female'),
	)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	#email_id=models.CharField(max_length=255,)

	date=models.DateField()
	hostler=models.BooleanField(default=False)
	sex = models.CharField(max_length=6,
		choices=SEX_CHOICES,
		default=MALE)
	email_id = models.EmailField()
	photo_img = models.FileField(upload_to='upload_file')
	classes=models.ForeignKey('Classes')
	english=models.PositiveIntegerField()
	tamil=models.PositiveIntegerField()
	maths=models.PositiveIntegerField()
	science=models.PositiveIntegerField()
	social=models.PositiveIntegerField()
	
class Classes(models.Model):
	id=models.AutoField(primary_key=True)
	classes=models.CharField(max_length=10)

	def __str__(self):
		return self.classes



	# classes_1= 'Class I'
	# classes_2= 'Class II'
	# classes_3= 'Class III'
	# classes_4= 'Class IV'
	# classes_5= 'Class V'
	# classes_6= 'Class VI'
	# classes_7= 'Class VII'
	# classes_8= 'Class VIII'
	# classes_9= 'Class IX'
	# classes_10= 'Class X'
	# classes_11= 'Class XI'
	# classes_12='Class XII'

	# Classes_choices=(
	# 	(classes_1, 'Class I'),
	# (classes_2, 'Class II'),
	# (classes_3, 'Class III'),
	# (classes_4, 'Class IV'),
	# (classes_5, 'Class V'),
	# (classes_6, 'Class VI'),
	# (classes_7, 'Class VII'),
	# (classes_8, 'Class VIII'),
	# (classes_9, 'Class IX'),
	# (classes_10, 'Class X'),
	# (classes_11, 'Class XI'),
	# (classes_12,'Class XII'),


	# 	),


	
	# classes=models.CharField(max_length=10,
	# 	choices=Classes_choices,
	# 	default=classes_1)

def __unicode__(self):
		return self.user.username