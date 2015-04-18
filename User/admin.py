from django.contrib import admin
from User.models import *
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Status)
admin.site.register(Order)

