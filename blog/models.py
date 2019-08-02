from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


class Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self): return self.name

class Tag(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self): return self.name


class Post(models.Model):
	content = models.CharField(max_length=1000)
	title = models.CharField(max_length=100)
	author = models.ForeignKey(User, 
		on_delete=models.CASCADE,related_name='posts')
	image = models.CharField(max_length=1000)
	category = models.ForeignKey(Category,
		on_delete=models.CASCADE, related_name='posts')
	published = models.DateField(default=date.today)
	tags = models.ManyToManyField(Tag, related_name='posts')
	views = models.IntegerField(default=0, editable=False)
	def __str__(self): return self.title
