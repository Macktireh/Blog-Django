from django import forms
from django.forms import fields
from .models import Blog, Comment


class Blogform(forms.ModelForm):
	class Meta:
		model = Comment
		fields = [
			'name',
			'email',
			'body'
		]
