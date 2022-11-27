from django.db import models
from django.contrib.auth.models import AbstractUser
from core.base_models import BaseEntity
from enum import Enum
# Create your models here.

class CustomUser(BaseEntity, AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class AccessEnum(Enum):
    Normal = 1
    Hr = 2
    Econ = 3


def is_normal_user(access_level):
    return access_level == AccessEnum.Normal.value


class UserAccess(BaseEntity):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.name


class ManagementUser(CustomUser):
    name = models.CharField(max_length=30, null=True)
    national_code = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField(null=True)
    salary = models.PositiveIntegerField(null=True, default=0)
    access_level = models.ForeignKey(UserAccess, to_field="id", on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.username


def get_all_users():
    return ManagementUser.objects.all()


def get_user_by_id(user_id):
    try:
        user = ManagementUser.objects.get(id=user_id)
        return user
    except:
        return None
