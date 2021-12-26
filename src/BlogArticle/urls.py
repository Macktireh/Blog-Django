from django.urls import path
from .views import List, article


urlpatterns = [
	path('', List.as_view(), name='home'),
	path('article/<slug:slug>', article, name='article'),
]