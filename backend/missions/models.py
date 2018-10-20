from django.db import models

from users.models import BaseModel, User


class Mission(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_missions', null=True)
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proposed_missions', null=True)
    amount = models.PositiveIntegerField(default=0, null=True)
    worker_approved = models.BooleanField(default=False, null=True)
    finished_by_worker = models.BooleanField(default=False, null=True)
    finished_by_customer = models.BooleanField(default=False, null=True)

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
