from django.contrib import admin
from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = 'title', 'created', 'author'
    search_fields = 'title', 'author'


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = 'text', 'question', 'created', 'author'
    search_fields = 'text', 'author'
