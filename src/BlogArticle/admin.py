from django.contrib import admin
from .models import Blog, Comment


admin.site.site_header = "Blog"
admin.site.site_title = "Interface Administrateur"
admin.site.index_title = "Blog"

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'intro', 'slug', 'date_added')
	search_fields = ('title',)


class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'body', 'date_added')
	search_fields = ('name', 'email',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)