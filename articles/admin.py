from django.contrib import admin
from .models import Article, Comment
# Register your models here.

admin.site.register(Article)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'post', 'created_on')
    list_filter = ('post', 'created_on')
    search_fields = ('user.name', 'post', 'body')

admin.site.register(Comment, CommentAdmin)