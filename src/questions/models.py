from django.db import models
from django.conf import settings
from categories.models import Category


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, blank=True, related_name='questions')
    is_archive = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='questions', on_delete=models.CASCADE)

    like_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    is_archive = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='answer', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)