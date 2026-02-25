from django.db import models, transaction
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model 
from django.db.models.manager import Manager
from django.utils.text import slugify
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.core.models import CommonModel
from utils.book import book_image_directory_path
from .signals import increase_book_review, decrease_book_review

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Categories"

    
class Book(CommonModel):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, related_name="books")
    authors = models.ManyToManyField("author.Author")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    upload_date = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey("core.Language", on_delete=models.SET_NULL, null=True)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    stock_quantity = models.PositiveIntegerField(default=0, null=True)
    num_of_pages = models.PositiveSmallIntegerField(default=100, null=True)
    description = models.TextField(null=True, blank=True)
    num_of_ratings = models.PositiveSmallIntegerField(default=0, null=True)

    def __str__(self):
        return self.title


class BookImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="images")
    is_primary = models.BooleanField(default=False)
    image_file = models.ImageField(upload_to=book_image_directory_path)

    def __str__(self):
        return str(self.book.title) + "'s image"
    
    def save(self, *args, **kwargs):
        if self.is_primary:
            with transaction.atomic():
                BookImage.objects.filter(book=self.book, is_primary=True).update(is_primary=False)
                super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

class BookPurchaseLinks(models.Model):
    link = models.CharField(max_length=500)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="pur_links")

    def __str__(self):
        return self.link[0:10]

class BookReviewManager(Manager):
    def get_queryset(self):
        return super().get_queryset()
    
    def with_replies(self):
        return super().get_queryset().prefetch_related("reviews")
    
    def popular(self):
        self.get_queryset().order_by("-likes")

class BookReview(CommonModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies")
    comment = models.TextField(null=True, blank=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book_reviews")
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=1, validators=[MinValueValidator(0), MaxValueValidator(5)])
    likes = models.PositiveIntegerField(default=0)
    dis_likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookReviewManager()

    def __str__(self):
        return f"{self.reviewer.username}'s review on {self.book.title}"


post_save.connect(increase_book_review, sender=BookReview)
post_delete.connect(decrease_book_review, sender=BookReview)
