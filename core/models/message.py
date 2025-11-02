from django.db import models
from .base import BaseModel
from django.conf import settings

class Message(BaseModel):
    conversation = models.ForeignKey(
        'core.Conversation',
        on_delete=models.CASCADE,
        related_name='messages'
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"From {self.sender}: {self.text[:30]}"