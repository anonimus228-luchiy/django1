from django.contrib import admin
from .models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at','author')
    list_filter = ('category',)
    list_editable = ('author',)

admin.site.register(Category)
admin.site.register(Tag)
