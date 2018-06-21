from django.db import models


class CategoryQuerySet(models.QuerySet):

    def aggregate_questions(self):
        return self.annotate(question_count=models.Count('questions__id'))


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CategoryQuerySet.as_manager()

    def __str__(self):
        return self.name
