from django.db import models
from django.contrib.auth.models import User
from core.base_models import BaseEntity
# Create your models here.


class UserAccess(BaseEntity):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=30)


class ManagementUser(BaseEntity):
    name = models.CharField(max_length=30, null=True)
    username = models.CharField(max_length=20, unique=True)
    national_code = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField(null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)
    access_level = models.ForeignKey(UserAccess, to_field="id", on_delete=models.SET_DEFAULT, default=1)


class Payment(BaseEntity):
    payment_date = models.DateField(unique=True)
    amount = models.PositiveIntegerField()
    owner = models.ForeignKey(ManagementUser, to_field="id", on_delete=models.CASCADE)