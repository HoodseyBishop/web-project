from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Question, Answer


def question_list(request):
    questions = Question.objects.all().filter(is_archive=False)
    context = {
        'questions': questions,
    }
    return render(request, 'questions/question_list.html', context)


def question_detail(request, pk=None):
    question = get_object_or_404(Question, id=pk)
    context = {
        'question': question,
        'answers': question.answers.all().filter(is_archive=False),
        'categories': question.categories.all(),
    }
    return render(request, 'questions/question_detail.html', context)