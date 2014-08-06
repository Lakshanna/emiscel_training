from django.db import models

# Create your models here.
class standard(models.Model):
	id=models.AutoField(primary_key=True)
	std=models.IntegerField() 

	def  __unicode__(self):
		return self.std

class district(models.Model):
	id=models.AutoField(primary_key=True)
	district=models.CharField(max_length=255)
	class Meta:
		unique_together=("id","district")

	def  __str__(self):
		return self.district

class block(models.Model):
	id=models.AutoField(primary_key=True)
	block_id=models.IntegerField()
	block=models.CharField(max_length=255)
	class Meta:
		unique_together=("id","block")

	def  __str__(self):
		return self.block
class school(models.Model):
	id=models.AutoField(primary_key=True)
	school_id=models.IntegerField()
	school=models.CharField(max_length=255,)
	class Meta:
		unique_together=("id","school")

	def  __str__(self):
		return self.school


class student(models.Model):
	roll_no=models.IntegerField()
	name=models.CharField(max_length=255,)
	std=models.ForeignKey(standard)
	school=models.ForeignKey(school)
	block=models.ForeignKey(block)
	district=models.ForeignKey(district)
	marks=models.IntegerField()

	def __unicode__(self):
		return ' '.join([self.name,self.fname,])

