from django.contrib import admin

from .models import BlogPost, PostComment
# Register your models here.
class PostCommentInline(admin.StackedInline):
    model = PostComment
class BlogPostAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    filedsets = [
    (None, {'fields': ['title']}),
    ('Body', {'fields': ['body']}),
    ('Post Information', {'fields': ['timestamp', 'author']}),
    ]
    inlines = [PostCommentInline]


admin.site.register(BlogPost, BlogPostAdmin)
