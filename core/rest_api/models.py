from django.db import models
from django.core import serializers

# Create your models here.

class ApiResponse:
    def __init__(self, success, message=[], data=None):
        self.success = success
        self.message = message
        self.data = data

    def __json__(self):
        return  {"success": self.success, "message": self.message, "data": self.data}


def serialize_users(users_models):
    return serializers.serialize('json', users_models)

