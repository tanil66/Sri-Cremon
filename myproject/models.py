from django.db import models

# Create your models here.

class Contact(models.Model):

	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	mobile = models.CharField(max_length=200)
	message = models.CharField(max_length=200)