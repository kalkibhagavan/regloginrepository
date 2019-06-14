from django.db import models

# Create your models here.
class rdata(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    uname=models.CharField(max_length=100)
    pword=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)