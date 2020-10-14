from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse 
from .models import *
from .forms import *
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# HOME-PAGE
def home_page(request):
	try:
		posts = Post.objects.order_by('-date')
		profile = get_object_or_404(Profile, user=request.user) 

		context = {
			'posts': posts, 
			'profile': profile
		}

	except:
		context = {
			'posts': posts, 
		}

	return render(request, 'index.html', context)


# ADD-POST PAGE
class PostCreatePage(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'thumbnail', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user.profile
		return super().form_valid(form)



	def get_success_url(self):
		return reverse('home')






# UPDATE-POST PAGE
class PostUpdatePage(UserPassesTestMixin, UpdateView, LoginRequiredMixin):
	model = Post
	fields = ['title', 'thumbnail', 'content']

	def test_func(self):

		post = self.get_object()

		if self.request.user.profile == post.author:
			return True
			
		else:
			return False


# DELETE-POST PAGE
class PostDeletePage(UserPassesTestMixin, DeleteView, LoginRequiredMixin):
	model = Post

	def test_func(self):

		post = self.get_object()

		if self.request.user.profile == post.author:
			print('Ant2')
			return True
			
		else:
			print("No Ant")
			return False
			
	
	def get_success_url(self):
		return reverse('home')



# SINGLE-POST PAGE
def post_single(request, id):
	post = get_object_or_404(Post, id=id)

	if post.likes.filter(id=request.user.id).exists():
		liked = True

	else:
		liked = False

	context = {
		'post': post,
		'liked': liked
	}

	return render(request, 'single-page.html', context)

# POST'S AUTHOR PAGE
def post_author(request, id):
	profile = get_object_or_404(Profile, id=id)

	context = {
		'profile': profile
	}

	return render(request, 'author.html', context)



# SEARCH-RESULTS PAGE
def search(request):
	query = request.GET.get('q')
	posts = Post.objects.all()

	if query:
		posts = posts.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query)
			).distinct()

	context = {
		'posts': posts
	}
	
	return render(request, 'search.html', context)

# GET POST LIKES
@login_required
def likes(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False

	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False

	else:
		post.likes.add(request.user)
		liked = True



	return HttpResponseRedirect(reverse('post', args=[str(pk)]))
