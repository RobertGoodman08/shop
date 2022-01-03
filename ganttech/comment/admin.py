from django.contrib import admin

from comment.models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'comment']
    list_display_links = ['username']
    list_filter = ['username']


admin.site.register(Comment, CommentAdmin)