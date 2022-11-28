from django.contrib import admin
from .models import UserAccess, ManagementUser, CustomUser
# Register your models here.

admin.site.register(UserAccess)
admin.site.register(ManagementUser)
admin.site.register(CustomUser)
