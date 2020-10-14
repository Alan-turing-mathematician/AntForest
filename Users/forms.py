from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Forest.models import Profile

class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]


class ProfileUpdate(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ["avatar", ]

	def __init__(self, *args, **kwargs):
		super(ProfileUpdate, self).__init__(*args, **kwargs)
		self.fields["avatar"].required = False



class UserUpdate(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username"]


	def __init__(self, *args, **kwargs):
		super(UserUpdate, self).__init__(*args, **kwargs)
		self.fields["username"].required = False