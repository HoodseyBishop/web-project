from django.shortcuts import render, HttpResponse
from categories.models import Category
from questions.models import Question


def main_page(request):
    context = {
        'questions': Question.objects.all().order_by('date_added')
    }
    return render(request, 'core/main.html', context)