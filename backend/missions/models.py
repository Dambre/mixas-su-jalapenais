import uuid
from django.db import models

from users.models import BaseModel, User


class Mission(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def as_dict(self):
        return {
            'uuid': self.uuid,
            'title': self.title,
            'description': self.description,
            'creator': self.creator_id,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
            }