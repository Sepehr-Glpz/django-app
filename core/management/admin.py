from django.contrib import admin
from .models import UserAccess, ManagementUser
# Register your models here.

admin.site.register(UserAccess)
admin.site.register(ManagementUser)
# admin.site.register(Payment)
