from django.db import models
# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=500)
    password=models.CharField(max_length=32) #len(MD5 Hash)=32
    email=models.CharField(max_length=200)
#class foss(models.Model):
    #

