from django.db import models
from .base import BaseModel
from django.conf import settings

class Conversation(BaseModel):
    ad = models.ForeignKey(
        'core.Ad',
        on_delete=models.CASCADE,
        related_name='conversations'
    )
    buyer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='buy_conversations'
    )
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sell_conversations'
    )

    class Meta:
        unique_together = ('ad', 'buyer', 'seller')

    def __str__(self):
        return f"{self.buyer} ↔ {self.seller} ({self.ad.title})"