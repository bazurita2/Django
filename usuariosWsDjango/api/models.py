from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
