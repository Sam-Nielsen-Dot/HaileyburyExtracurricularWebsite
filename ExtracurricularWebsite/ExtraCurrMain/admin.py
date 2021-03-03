from django.contrib import admin
from .models import User, Post
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "timestamp", "content")


#registering models
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
