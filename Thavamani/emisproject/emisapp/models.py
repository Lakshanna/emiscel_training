from django.db import models
from django.contrib.auth.models import User
class scommunity(models.Model):
	commid=models.IntegerField(primary_key=True)
	scomm=models.CharField(max_length=30)
	def __unicode__(self):
		return self.scomm
class caste(models.Model):
	casteid=models.IntegerField(primary_key=True)
	scaste=models.CharField(max_length=30,default='Select')
	def __unicode__(self):
		return self.scaste
class religion(models.Model):
	relid=models.IntegerField(primary_key=True)
	srel=models.CharField(max_length=30,default='Select')
	def __unicode__(self):
		return self.srel
class language(models.Model):
	lanid=models.IntegerField(primary_key=True)
	slan=models.CharField(max_length=30,default='Select')
	def __unicode__(self):
		return self.slan
class differently_abled(models.Model):
	daid=models.IntegerField(primary_key=True)
	sdabled=models.CharField(max_length=30,default='Select')
	def __unicode__(self):
		return self.sdabled

class nationality(models.Model):
	nationid=models.IntegerField(primary_key=True)
	snation=models.CharField(max_length=30,default='Select')
	def __unicode__(self):
		return self.snation
class bloodgroup(models.Model):
	bgid=models.IntegerField(primary_key=True)
	sbg=models.CharField(max_length=30,default='Select')
	def __unicode__(self):
		return self.sbg

class moccupation(models.Model):
	soccid=models.IntegerField(primary_key=True)
	smocc=models.CharField(max_length=30,default='Select')
	def __unicode__(self):
		return self.smocc
class foccupation(models.Model):
	foccid=models.IntegerField(primary_key=True)
	sfocc=models.CharField(max_length=30,default='Select')
	def __unicode__(self):
		return self.sfocc
class class_studying(models.Model):
	classid=models.IntegerField(primary_key=True)
	sclass=models.CharField(max_length=30)
	def __unicode__(self):
		return self.sclass
class section(models.Model):
	secid=models.IntegerField(primary_key=True)
	ssection=models.CharField(max_length=30)
	def __unicode__(self):
		return self.ssection
class medium(models.Model):
	medid=models.IntegerField(primary_key=True)
	smedium=models.CharField(max_length=30)
	def __unicode__(self):
		return self.smedium
class district(models.Model):
	distid=models.IntegerField(primary_key=True)
	sdistrict=models.CharField(max_length=30)
	def __unicode__(self):
		return self.sdistrict
class block(models.Model):
	blockid=models.IntegerField(primary_key=True)
	sblock=models.CharField(max_length=30)
	def __unicode__(self):
		return self.sblock
class bank(models.Model):
	bankid=models.IntegerField(primary_key=True)
	sbank=models.CharField(max_length=30)
	def __unicode__(self):
		return self.sbank
class sports(models.Model):
	spid=models.IntegerField(primary_key=True)
	ssname=models.CharField(max_length=30)
	def __unicode__(self):
		return self.ssname
class academicyear(models.Model):
	acyid=models.IntegerField(primary_key=True)
	aayear=models.CharField(max_length=30)
	def __unicode__(self):
		return self.aayear
class studenttable(models.Model):
	sid=models.CharField(primary_key=True, max_length=30)
	sname=models.CharField(max_length=30)
	sphoto = models.FileField(upload_to='hi/test')
	sdob=models.DateField()
	scomm=models.ForeignKey(scommunity)
	scommcert=models.BooleanField(default=False)
	srel=models.ForeignKey(religion)
	slan=models.ForeignKey(language)
	sphone=models.IntegerField()
	sdis=models.BooleanField(default=False)
	sdabled=models.ForeignKey(differently_abled)
	scaste=models.ForeignKey(caste)
	snation=models.ForeignKey(nationality)
	spin=models.IntegerField()
	sbg=models.ForeignKey(bloodgroup)
	smother=models.CharField(max_length=50)
	smocc=models.ForeignKey(moccupation)
	smincome=models.IntegerField()
	sfather=models.CharField(max_length=50)
	sfocc=models.ForeignKey(foccupation)
	sfincome=models.IntegerField()
	sclass=models.ForeignKey(class_studying)
	ssection=models.ForeignKey(section)
	smedium=models.ForeignKey(medium)
	sdistrict=models.ForeignKey(district)
	sblock=models.ForeignKey(block)
	sschool=models.CharField(max_length=100)
	sscode=models.IntegerField()
	sbank=models.ForeignKey(bank)
	saccno=models.IntegerField()
	ssports=models.BooleanField(default=False)
	ssname=models.ForeignKey(sports)
	aayear=models.ForeignKey(academicyear)
	def __unicode__(self):
		return self.sid

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    company = models.CharField(max_length=250,blank=True)
    website = models.URLField(blank=True)
    def __unicode__(self):
        return self.user.username