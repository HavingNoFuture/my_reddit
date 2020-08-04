from django.contrib import admin

from reddit.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__", "pub_date")
    list_display_links = ("id", "__str__")
    readonly_fields = ('author', 'rating', 'pub_date', 'slug')
