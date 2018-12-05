from django.db import models


class User(models.Model):
	nickname = models.CharField(max_length=30)
	somebody = models.CharField(max_length=30)
	motion = models.CharField(max_length=30)
	message = models.TextField()
	gender = models.CharField(max_length=30)
	avatar = models.ImageField(null=True,blank=True,upload_to='media/icon')
	date1 = models.DateField()
# Create your models here.
