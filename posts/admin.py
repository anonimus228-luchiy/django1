from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image_tag', 'created_at')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:5px;" />',
                               obj.image.url)
        return format_html('<img src="/static/images/placeholder.png" width="50" height="50" />')

    image_tag.short_description = 'Image'


admin.site.register(Category)
admin.site.register(Tag)
