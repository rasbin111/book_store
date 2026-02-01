from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):
    author_id = models.CharField(max_length=100, unique=True)
    name = models.CharField()
    average_reviews = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    followers_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
