from django.db import models

from app.models import DefaultModel

# Create your models here.


class Author(DefaultModel):
    name = models.CharField(max_length=100)
    image = models.ImageField()
