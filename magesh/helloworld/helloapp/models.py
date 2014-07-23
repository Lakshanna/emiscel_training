from django.db import models

# Create your models here.
class  student(models.Model):
	roll_no=models.IntegerField()
	admin_dt=models.DateField(auto_now=False, auto_now_add=False)
	fname=models.CharField(max_length=255,)
	lname=models.CharField(max_length=255,)
	is_spl_stu=models.BooleanField( default="False")
	photo=models.FileField(upload_to="upload")
	email=models.EmailField(max_length=254)

	def __unicode__(self):
		return ' '.join([self.fname,self.lname,])
