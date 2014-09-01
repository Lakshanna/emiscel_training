from django.db import models

# Create your models here.

class Blocktable(models.Model):
	Sl_No=models.IntegerField()
	Block = models.IntegerField()
	Block_Name = models.CharField(max_length=100,primary_key=True)

class Schoollist(models.Model):
	Districtname=models.CharField(max_length=500)
	Blockname=models.CharField(max_length=500)
	UDISEcode=models.BigIntegerField(primary_key=True)
	Schoolname=models.CharField(max_length=100)
	Management=models.CharField(max_length=500)
	Category=models.CharField(max_length=500)
	Girlsstrength=models.IntegerField()
	Boysstrength=models.IntegerField()
	Girlstoilet=models.IntegerField()
	Boystoilet=models.IntegerField()
	Girlsworking=models.IntegerField()
	Boysworking=models.IntegerField()
	def __str__(self):
		return self.Districtname

class District(models.Model):
	Districtname=models.CharField(max_length=50,primary_key=True)
class Block(models.Model):
 	Blockname=models.CharField(max_length=50,primary_key=True)
# class Schoollist_new(models.Model):
# 	Districtname=models.ForeignKey(District)
# 	Blockname=models.ForeignKey(Block)
# 	UDISEcode=models.BigIntegerField(primary_key=True)
# 	Schoolname=models.CharField(max_length=100)
# 	Management=models.CharField(max_length=50)
# 	Category=models.CharField(max_length=50)