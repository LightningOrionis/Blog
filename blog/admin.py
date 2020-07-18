from django.contrib import admin
from .models import Post, Blogger, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ('rating',)
    list_display = ('title', 'rating', 'author')
    list_filter = ('author', )


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('author', 'get_subscribers_count')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'rating',)
    exclude = ('rating', )
