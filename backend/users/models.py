import uuid

from django.db import models
from django.contrib.auth.models import User as AuthUser
from annoying.fields import AutoOneToOneField


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):
    user = AutoOneToOneField(AuthUser, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
