from django.contrib import admin
from django.contrib.auth import get_user_model

from reddit.models import Post

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")
    list_display_links = ("username", "id")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__", "pub_date")
    list_display_links = ("id", "__str__")
