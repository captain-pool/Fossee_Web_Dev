from django.db import models
# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=500)
    password=models.CharField(max_length=32) #len(MD5 Hash)=32
    email=models.CharField(max_length=200)
class foss(models.Model):
	name=models.CharField(max_length=1000)
class tutorial_detail(models.Model):
	foss=models.ForeignKey(foss,on_delete=models.CASCADE)
	tutorial_name=models.CharField(max_length=1000)
	expected_submission_date=models.DateField()
	actual_submission_date=models.DateField()
	contributor=models.ForeignKey(user,on_delete=models.CASCADE)
class payment(models.Model):
	contributor=models.ForeignKey(user,on_delete=models.CASCADE)
	payment=models.IntegerField()
