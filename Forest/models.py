from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from PIL import Image


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='avatars', blank=True)

	def __str__(self):
		return self.user.username


class Post(models.Model):
	author = models.OneToOneField(Profile, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	content = models.TextField()
	thumbnail = models.ImageField(upload_to='thumbnails', blank=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.OneToOneField(Post, on_delete=models.CASCADE)
	author = models.OneToOneField(Profile, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title

































