from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)