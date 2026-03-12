from django.contrib import admin

from .models import   DeliveryPerson, UserAddress, UserOrder

admin.site.register([DeliveryPerson, UserAddress, UserOrder])
