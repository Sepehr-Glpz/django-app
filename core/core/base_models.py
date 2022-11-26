from django.db import models
import uuid

class BaseEntity(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField("id", primary_key=True, default=uuid.uuid4)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)