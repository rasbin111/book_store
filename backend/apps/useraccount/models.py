import uuid
from decimal import Decimal, ROUND_HALF_UP
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator

from utils.validators import PHONE_REGEX
from utils.user import get_unique_username, user_avatar_directory_path

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
        ('viewer', 'viewer'),
        ('delivery', 'delivery_person')
    )
    GENDER_CHOICES = ((0, "Male"), (1, "Female"), (2, "Other"))

    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=10, default="viewer", choices=USER_ROLES_CHOICES)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    avatar = models.ImageField(upload_to=user_avatar_directory_path, null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
    
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


class DeliveryPerson(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    user= models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING, null=True)
    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    street_address = models.CharField(max_length=255, null=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True, validators=[PHONE_REGEX,])
    alt_phone_number = models.CharField(max_length=15, null=True, blank=True, validators=[PHONE_REGEX,])


    def __str__(self):
        return self.full_name

class UserAddress(models.Model):
    ADRESS_TYPE_CHOICES = (
        (0, "Home"),
        (1, "Office"),
        (2, "Other"),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address_type = models.PositiveSmallIntegerField(choices=ADRESS_TYPE_CHOICES, default=0)
    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    street_address = models.CharField(max_length=255, null=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True, validators=[PHONE_REGEX,])
    alt_phone_number = models.CharField(max_length=15, null=True, blank=True, validators=[PHONE_REGEX,])
    
    # Skipped this for now (from django.contrib.gis.db import models)
    # location = models.PointField(blank=True, null=True) 

    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s address: {self.address}"
    

class UserOrder(models.Model):
    ORDER_STATUS_CHOICES = (
        (0, "pending"),
        (1, "ordered"),
        (2, "processing"),
        (3, "shipped"),
        (4, "delivered"),
        (5, "cancelled"),
        (6, "returned"),
        (7, "refunded"),
    )
    PAYMENT_STATUS_CHOICES = (
        (0, "pending"),
        (2, "paid"),
        (3, "failed"),
        (4, "refunded"),
    )
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="orders")
    address = models.OneToOneField(UserAddress, on_delete=models.CASCADE)
    order_status = models.PositiveSmallIntegerField(choices=ORDER_STATUS_CHOICES, default=0)
    payment_status = models.PositiveSmallIntegerField(choices=PAYMENT_STATUS_CHOICES, default=0)
    order_amount = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, blank=True, null=True)
    tax = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, validators=[
        MinValueValidator(0.00), MaxValueValidator(100.00)
    ], blank=True, null=True)
    delivery_charge = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, null=True, blank=True)
    paid_amount = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, null=True, blank=True)
    delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="orders")

    def __str__(self):
        return f"{self.user.username}'s order: {self.oder_id}"
    
    def save(self, *args, **kwargs):
        tax_amount = tax_amount = (self.tax * self.order_amount) / Decimal('100')
        total = self.order_amount + tax_amount + self.delivery_charge

        # If a total is 10.555, ROUND_HALF_UP makes it 10.56
        self.total_amount = total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)  # Decimal("0.01")   tells python to where to round   
        
        return super().save(*args, **kwargs)

class UserLoginTrack(models.Model):
    user = models.ForeignKey(CustomUser, related_name="login_track", on_delete=models.CASCADE)
    user_agent = models.CharField(max_length=700, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    browser_name = models.CharField(max_length=255, null=True, blank=True)
    browser_version = models.CharField(max_length=255, blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    device = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=False, null=True)
    last_login = models.DateTimeField(auto_now=True, null=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s track: {self.ip_address}"
    
    def save(self, *args, **kwargs):
        user = self.user 
        active_sessions = self.__class__.objects.filter(
            user=user,
            is_active=True
        ).order_by("-created_at")

        if active_sessions.count() >= 5:
            oldest_session = active_sessions.last()
            oldest_session.is_active = False

        return super().save(*args, **kwargs)