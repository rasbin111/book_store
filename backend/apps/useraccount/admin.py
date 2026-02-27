from django.contrib import admin

from .models import CustomUser, UserLoginTrack, DeliveryPerson, UserAddress, UserOrder

admin.site.register(CustomUser)
admin.site.register(UserLoginTrack)
admin.site.register([DeliveryPerson, UserAddress, UserOrder])
