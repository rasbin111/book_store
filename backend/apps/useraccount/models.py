from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import timedelta

from utils.validators import PHONE_REGEX


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

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff = True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser = True")

        return self.create_user(email, password, username, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True, validators=[PHONE_REGEX, ])
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.name