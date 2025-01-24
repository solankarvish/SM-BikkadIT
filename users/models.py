from django.db import models

# Create your models here.
class Registration(models.Model):
    fname = models.CharField(max_length=20)
    mname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    qualification = models.CharField(max_length=20)
    batch = models.CharField(max_length=20)
    passingyear=models.DateField()
    email = models.EmailField()
    mobnumber = models.IntegerField()
    dist = models.CharField(max_length=15)
    