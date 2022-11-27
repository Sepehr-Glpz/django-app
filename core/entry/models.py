from django.db import models
from core.base_models import BaseEntity
# Create your models here.


class EntryRequest(BaseEntity):
    email = models.EmailField(unique=True)
    resolved = models.BooleanField(default=False)


def get_request_by_email(email):
    try:
        requested_user = EntryRequest.objects.get(email=email)
        return requested_user, None
    except :
        return None, "Failed to Find User"


def resolve_entry(entry_id):
    try:
        updated_entry = EntryRequest.objects.filter(id=entry_id).update(resolved=True)
    except:
        return
