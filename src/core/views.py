from django.shortcuts import render, HttpResponse
from categories.models import Category
from questions.models import Question


def main_page(request):
    return render(request, 'core/main.html', {})