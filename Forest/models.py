from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from PIL import Image



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='avatars', blank=True)

	def get_absolute_url(self):
		return reverse('author', kwargs={
				'id': self.id
			})

	def get_absolute_url2(self):
		return reverse('profile', kwargs={
				'id': self.id
			})

	def get_posts(self):
		return self.posts.all()

	def __str__(self):
		return self.user.username



class Post(models.Model):
	author = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)
	title = models.CharField(max_length=500)
	content = models.TextField()
	thumbnail = models.ImageField(upload_to='thumbnails', blank=True)
	date = models.DateTimeField(auto_now_add=True)
	likes = models.ManyToManyField(User, related_name='post_likes')

	def count_likes(self):
		return self.likes.count()


	def get_absolute_url(self):
		return reverse('post', kwargs={
			'id': self.id
			})


	def get_absolute_url2(self):
		return reverse('update', kwargs={
			'pk': self.id
			})

	def get_absolute_url3(self):
		return reverse('delete', kwargs={
			'pk': self.id
			})

	def get_comments(self):
		return self.comments.all()

	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	author = models.ForeignKey(Profile, on_delete=models.CASCADE)
	content = models.TextField() 

	def __str__(self):
		return self.content

































