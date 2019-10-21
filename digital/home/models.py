from django.db import models   

# Create your models here.

class Register(models.Model):
	Name = models.CharField(max_length = 25)
	Email = models.CharField(max_length = 25)
	Phone_no = models.CharField(max_length = 10)
	Course = models.CharField(max_length = 25)
	Source = models.CharField(max_length = 25)
	Leadstatus = models.CharField(max_length = 25)
	Date_demo = models.CharField(max_length = 25)
	Counsler = models.CharField(max_length = 25)
	Remark = models.CharField(max_length = 25)

	def __str__(self):
		return self.Name

class Joining(models.Model):
	name = models.CharField(max_length = 25)
	course = models.CharField(max_length = 25)
	Completion_Date = models.CharField(max_length = 25)
	Date_joining = models.CharField(max_length = 25)
	Course_fee = models.CharField(max_length = 25)
	Instructor = models.CharField(max_length = 25)
	Aadhar_no = models.CharField(max_length = 25)
	email = models.CharField(max_length = 25)
	phone_no = models.CharField(max_length = 25)
	remark = models.CharField(max_length = 25)
	status = models.CharField(max_length=20)
	def __str__(self):
		return self.name