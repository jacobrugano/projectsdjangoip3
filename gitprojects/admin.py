from django.contrib import admin

# Register your models here.
from .models import Category, Project

admin.site.register(Category)
admin.site.register(Project)