from django.db import models
from .base import BaseModel


class City(BaseModel):
    name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.name