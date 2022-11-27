from django.db import models
from django.contrib.auth.models import AbstractUser
from core.base_models import BaseEntity
# Create your models here.

class CustomUser(BaseEntity, AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=64)
    email = models.EmailField(unique=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

class UserAccess(BaseEntity):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=30)


class ManagementUser(CustomUser):
    name = models.CharField(max_length=30, null=True)
    national_code = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField(null=True)
    salary = models.PositiveIntegerField(null=True)
    access_level = models.ForeignKey(UserAccess, to_field="id", on_delete=models.SET_DEFAULT, default=1)


# class Payment(BaseEntity):
#     payment_date = models.DateField(unique=True)
#     amount = models.PositiveIntegerField()
#     owner = models.ForeignKey(ManagementUser, null=True, to_field="id", on_delete=models.CASCADE)