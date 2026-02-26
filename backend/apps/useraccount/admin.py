from django.contrib import admin

from .models import CustomUser, UserLoginTrack

admin.site.register(CustomUser)
admin.site.register(UserLoginTrack)
