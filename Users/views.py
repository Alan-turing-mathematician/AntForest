from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from Forest.models import Profile
from django.contrib.auth.decorators import login_required

# REGISTRATION-PAGE
def register_page(request):
	
	if request.method == 'POST':
		form = RegisterForm(request.POST)

		if form.is_valid():
			form.save()

			return redirect('login')

	else:
		form = RegisterForm()

	context = {
		'form': form
	}

	return render(request, 'register.html', context)

# PROFILE-PAGE
@login_required
def profile(request, id):
	profile = get_object_or_404(Profile, id=id)

	if request.method == 'POST':
		form = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
		form2 = UserUpdate(request.POST, request.FILES, instance=request.user)

		if form.is_valid and form2.is_valid():
			form2.save()
			form.save()

	else:
		form2 = UserUpdate(instance=request.user)
		form = ProfileUpdate(instance=request.user.profile)

	context = {
		'profile': profile,
		'form': form,
		'form2': form2
	}

	return render(request, 'profile.html', context)