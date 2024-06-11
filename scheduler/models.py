from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class faculty(models.Model):
    fac_id = models.CharField(max_length=10,primary_key=True)
    fac_name = models.CharField(max_length=100,null=False)

class subject(models.Model):
    sub_code = models.CharField(max_length=10,primary_key=True)
    sub_name = models.CharField(max_length=100,null=False)
    sub_cat = models.CharField(max_length=100,null=False)
    fac_1 = models.CharField(max_length=10,null=False)
    fac_2 = models.CharField(max_length=10)
    fac_3 = models.CharField(max_length=10)
    room = models.CharField(max_length=10,null=False)

class runningbatches(models.Model):
    batch = models.CharField(max_length=20)
    school = models.CharField(max_length=20)
    division = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)
    nsubs = models.IntegerField(max_length=20)
  
class slot(models.Model):
    sname = models.CharField(max_length=5)
    starttime = models.TimeField()
    endtime = models.TimeField()

class example(models.Model):
    sname = models.CharField(max_length=5)
    starttime = models.TimeField()