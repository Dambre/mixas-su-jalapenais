import uuid

from django.db import models
from django.contrib.auth.models import User as AuthUser


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DatetimeField(auto_now_add=True)
    updatedAt = models.EmailField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
