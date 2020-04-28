from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    chosen = models.BooleanField(default=False)

class Skills(models.Model):
    languages=models.CharField(max_length=30)
    User = models.ManyToManyField(User)
    def __str__(self):
        return(self.languages)

class Squad(models.Model)