from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    languages = models.CharField(max_length=30)
