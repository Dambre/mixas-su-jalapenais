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


USER_TYPES = (
    ('customer', 'Customer'),
    ('worker', 'Worker'),
)


class User(BaseModel):
    user = AutoOneToOneField(AuthUser, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    firstName = models.CharField(max_length=50, null=True, blank=True)
    lastName = models.CharField(max_length=50, null=True, blank=True)
    userType = models.CharField(choices=USER_TYPES, max_length=20, default='Customer')

    def as_dict(self):
        return {
            'uuid': self.uuid,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
            'email': self.email,
            'firstName': self.firstName,
            'lastName': self.lastName,
        }
