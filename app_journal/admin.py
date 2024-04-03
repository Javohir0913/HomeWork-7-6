from django.contrib import admin

from .models import Category, Journal

# Register your models here.
admin.site.register(Category)
admin.site.register(Journal)
