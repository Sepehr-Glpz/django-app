from django.db import models
from core.base_models import BaseEntity
from django.core.exceptions import ObjectDoesNotExist
from uuid import UUID
# Create your models here.


class EntryRequest(BaseEntity):
    email = models.EmailField(unique=True)
    resolved = models.BooleanField(default=False)


def get_request_by_email(email):
    try:
        requested_user = EntryRequest.objects.get(email=email)
        return requested_user
    except ObjectDoesNotExist:
        return None


def entry_repeated(request):
    return request is not None


def get_request_by_id(request_id):
    try:
        request = EntryRequest.objects.get(id=request_id)
        return request, None
    except:
        return None, "Failed to find request"


def resolve_entry(entry_id):
    try:
        updated_entry = EntryRequest.objects.filter(id=entry_id).update(resolved=True)
    except:
        return


def convert_id(user_id):
    try:
        uuid_obj = UUID(user_id, version=4)
        return uuid_obj
    except ValueError:
        return None


def validate_password(data_dict):
    password = data_dict["password"]
    confirmation = data_dict["confirm_password"]
    if password != confirmation:
        return False
    return True
