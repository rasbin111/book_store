import uuid
from django.db import models
from django.contrib.auth import get_user_model
from decimal import Decimal, ROUND_HALF_UP
from django.core.validators import MinValueValidator, MaxValueValidator

from utils.validators import PHONE_REGEX
from utils.sale import default_delivery_date

User = get_user_model()


class DeliveryPerson(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    user= models.OneToOneField(User, on_delete=models.DO_NOTHING, null=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_type = models.PositiveSmallIntegerField(choices=ADRESS_TYPE_CHOICES, default=0)
    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    street = models.CharField(max_length=255, null=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
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
    expected_delivery_date = models.DateField(default=default_delivery_date, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s order: {self.oder_id}"
    
    def save(self, *args, **kwargs):
        tax_amount = tax_amount = (self.tax * self.order_amount) / Decimal('100')
        total = self.order_amount + tax_amount + self.delivery_charge

        # If a total is 10.555, ROUND_HALF_UP makes it 10.56
        self.total_amount = total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)  # Decimal("0.01")   tells python to where to round   
        
        return super().save(*args, **kwargs)

