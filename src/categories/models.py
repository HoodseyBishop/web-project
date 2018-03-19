from django.db import models
# from questions.models import Question


class Category(models.Model):
    name = models.CharField(max_length=255)
    # questions = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return self.name
