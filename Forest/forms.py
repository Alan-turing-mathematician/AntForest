from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CommentForm(forms.ModelForm):
	class Meta:

		model = Comment
		fields = ['content', ]