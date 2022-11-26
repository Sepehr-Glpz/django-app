from django.db import models
from core.base_models import BaseEntity
# Create your models here.


class EntryRequest(BaseEntity):
    email = models.EmailField(unique=True)
    resolved = models.BooleanField(default=False)

