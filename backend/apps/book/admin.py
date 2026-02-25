from django.contrib import admin

# Register your models here.
from .models import Category, Book, BookImage, BookReview

admin.site.register([Category, Book, BookImage, BookReview])
