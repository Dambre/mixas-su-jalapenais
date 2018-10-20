import uuid
from django.db import models

from users.models import BaseModel, User


class Mission(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    creator = models.ForeignKey(User)