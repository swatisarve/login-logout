from django.db import models

# Create your models here.
class Result(models.Model):
    firstname=models.CharField(max_length=120)
    lastname=models.CharField(max_length=120)
    emailid=models.CharField(max_length=120)
    mobilenumber=models.CharField(max_length=120)
    gender=models.CharField(max_length=120)