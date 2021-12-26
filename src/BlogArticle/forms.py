from django import forms
from .models import Blog, Comment


class Blogform(forms.ModelForm):

	class Meta:
		model = Comment
		fields = [
			'name',
			'email',
			'body',
		]
