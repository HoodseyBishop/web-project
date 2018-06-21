from django.db import models
from django.conf import settings


class Like(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey('questions.Question', related_name='likes', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('author', 'question')
