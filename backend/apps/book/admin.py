from django.contrib import admin

# Register your models here.
from .models import Category, Book, BookImage

admin.site.register([Category, Book, BookImage])
