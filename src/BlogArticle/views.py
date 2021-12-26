from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog, Comment
from .forms import Blogform


class List(ListView):
	template_name = 'BlogArticle/home/index.html'
	queryset = Blog.objects.all()
	paginate_by = 2


def article(request, slug):
	article = Blog.objects.get(slug=slug)
	comments = article.comments.all()
	if request.method == 'POST':
		form = Blogform(request.POST)
		if form.is_valid():
			form.save(commit=False)
			form.instance.post = article
			form.save()
			return redirect('article', slug=article.slug)
	else:
		form = Blogform()

	doc = 'BlogArticle/article/index.html'

	context = {
		'article': article,
		'comments': comments,
		'form': form
		}

	return render(request, doc, context)