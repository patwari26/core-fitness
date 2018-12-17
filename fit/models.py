from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Person(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    height=models.FloatField()
    weight=models.FloatField()
    bmi=models.FloatField(null=True,blank=True)

class Tips(models.Model):
    tip=models.CharField(max_length=10)
    def __str__(self):
        return self.tip
class Cataegory_tips(models.Model):
    category=models.CharField(max_length=10)
    mortips=models.ManyToManyField(Tips,related_name='mor')
    noontips = models.ManyToManyField(Tips,related_name='noon')
    exercices=models.ManyToManyField(Tips,related_name='exe')
    dintips = models.ManyToManyField(Tips,related_name='din')

    def __str__(self):
        return self.category
