from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse 
from .models import *

# HOME-PAGE
def home_page(request):
	posts = Post.objects.order_by('-date')

	context = {
		'posts': posts
	}
	return render(request, 'index.html', context)


# SIGN-UP PAGE
class RegisterPage(CreateView):
	model = User
	email = models.EmailField()
	fields = ['username', 'email', 'password']

	def get_success_url(self):
		return reverse('home')



# ADD-POST PAGE
class PostCreatePage(CreateView):
	model = Post
	fields = ['title', 'thumbnail', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user.profile
		return super().form_valid(form)



	def get_success_url(self):
		return reverse('home')

