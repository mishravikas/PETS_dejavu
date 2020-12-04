from django.db import models

# Create your models here.
class Link(models.Model):
	url = models.CharField(max_length=500)
	rank = models.CharField(max_length=500,null=True)
	website = models.CharField(max_length=500)
	secret = models.CharField(max_length=500,null=True)
	vw = models.CharField(max_length=500,null=True)
	inUse = models.BooleanField(default=False)

class Resource(models.Model):
	url = models.CharField(max_length=500)
	rank = models.CharField(max_length=500,null=True)
	website = models.CharField(max_length=500)
	secret = models.CharField(max_length=500,null=True)
	vw = models.CharField(max_length=500,null=True)
	inUse = models.BooleanField(default=False)

class Person(models.Model):
	hash = models.CharField(max_length=500)
	
	