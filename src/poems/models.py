from django.db import models

from app.models import DefaultModel
from authors.models import Author


class Poem(DefaultModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=150)


class Screen(DefaultModel):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True)
