from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class login(models.Model):
# 	uid=models.CharField(primary_key=True,max_length=30)
# 	pwd=models.CharField(max_length=30)

# 	def __unicode__(self):
# 		return self.uid
	

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    company = models.CharField(max_length=250,blank=True)
    website = models.URLField(blank=True)
    def __unicode__(self):
        return self.user.username

class class_studying(models.Model):
	classid=models.IntegerField(primary_key=True)
	classes=models.CharField(max_length=30)
	def __unicode__(self):
		return self.classid
class class_studying1(models.Model):
    
    classes=models.CharField(max_length=30)
    def __unicode__(self):
        return self.classes

class studenttable(models.Model):
    studentid=models.CharField(primary_key=True, max_length=30)
    studnetname=models.CharField(max_length=30)
    fathername=models.CharField(max_length=30)
    schoolname=models.CharField(max_length=30)
    classes=models.ForeignKey(class_studying1)
    computer=models.IntegerField()
    physics=models.IntegerField()
    chemistry=models.IntegerField()
    maths=models.IntegerField()
    total=models.IntegerField()

    def __unicode__(self):
		return self.studentid
     