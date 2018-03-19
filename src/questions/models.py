from django.db import models
from django.conf import settings
from categories.models import Category


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created = models.DateTimeField(auto_created=True)
    categories = models.ManyToManyField(Category, blank=True)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.title