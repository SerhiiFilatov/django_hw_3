from django.contrib import admin

from .models import *


# @admin.register(Post)
class Post_admin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Headings)
class Headings_admin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Post, Post_admin)