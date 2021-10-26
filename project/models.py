from django.db import models
# Create your models here.
class login (models.Model):
    nik = models.IntegerField(max_length=20)
    password = models.CharField(max_length=8)