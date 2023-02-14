from django.contrib import admin

from .models import *


@admin.register(User_model)
class User_model(admin.ModelAdmin):
    ...