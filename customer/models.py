from django.db import models
from django.db.models.fields import CharField, IntegerField

class Customer(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    tp_number = models.IntegerField()
    profile_pic = models.CharField(max_length=2083)


class Register(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField()
    date = models.DateField()
