from django.db import models


class User(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	ip = models.GenericIPAddressField()
	icon = models.ImageField(null=True,blank=True,upload_to='icon')
	phonenumber = models.CharField(max_length=30)
# Create your models here.
