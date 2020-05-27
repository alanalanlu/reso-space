from django.db import models

# Create your models here.


class Squad(models.Model):
    #member=models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
    pass


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    chosen = models.BooleanField(default=False)
    team=models.ForeignKey(Squad,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.name

class Skills(models.Model):
    languages=models.CharField(max_length=30)
    User = models.ManyToManyField(User,related_name="skill",blank=True)
    def __str__(self):
        return self.languages

