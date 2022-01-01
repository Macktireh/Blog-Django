from django.db import models
from django.db.models.fields.related import ForeignKey
from ckeditor.fields import RichTextField


class Blog(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField()
	intro = RichTextField()
	body = RichTextField()
	image = models.ImageField(upload_to='media')
	date_added = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-date_added']


class Comment(models.Model):
	post = ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
	name = models.CharField(max_length=128, default='inconnu')
	email = models.EmailField()
	body = RichTextField()
	date_added = models.DateTimeField(auto_now=True)


	class Meta:
		ordering = ['-date_added']
