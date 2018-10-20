from django.db import models

from users.models import BaseModel, User


class Mission(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    specialist = models.ForeignKey(User, )
    specialist_approved = models.BooleanField(default=False)

    def as_dict(self):
        return {
            'uuid': self.uuid,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
            'title': self.title,
            'description': self.description,
            'amount': self.amount,
            'creator': self.creator.as_dict(),
        }


class Bid(BaseModel):
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='bids')
    amount = models.PositiveIntegerField(default=0)

    def as_dict(self):
        return {
            'uuid': self.uuid,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
            'amount': self.amount,
            'worker': self.worker.as_dict(),
            'mission': self.mission.as_dict(),
        }

