from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import timedelta

from utils.validators import PHONE_REGEX
from utils.user import get_unique_username


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, email, password=None, username=None, **extra_fields):
        if not email:
            raise ValueError("Email is Required")
        user = self.model(email=self.normalize_email(email), username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("role", "superuser")

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff = True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser = True")

        return self.create_user(email, password, username, **extra_fields)


class CustomUser(AbstractUser):
    USER_ROLES_CHOICES = (
        ('superuser', 'superuser'),
        ('admin', 'admin'),
        ('editor', 'editor'),
        ('viewer', 'viewer')
    )
    GENDER_CHOICES = ((0, "Male"), (1, "Female"), (2, "Other"))

    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=10, default="viewer", choices=USER_ROLES_CHOICES)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, default=0)
    phone_number = models.CharField(max_length=15, null=True, blank=True, validators=[PHONE_REGEX, ])
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.name
    
    @property
    def get_gender_value(self):
        return self.get_gender_display()
    

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()

        if not self.username:
            self.username = get_unique_username(self, self.first_name + " " + self.last_name, "username")

        return super().save(*args, **kwargs)