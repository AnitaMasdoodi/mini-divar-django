from django.db import models
from django.conf import settings
from django.utils.text import slugify
from .base import BaseModel

class Ad(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ads'
    )
    category = models.ForeignKey(
        'core.Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='ads'
    )
    city = models.ForeignKey(
        'core.City',
        on_delete=models.SET_NULL,
        null=True,
        related_name='ads'
    )
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='ads/')
    price = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Ad.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title