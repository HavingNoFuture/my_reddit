from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


# Register your models here.
@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")
    list_display_links = ("username", "id")
