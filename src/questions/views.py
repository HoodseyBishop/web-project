from django.shortcuts import render, HttpResponse

# Create your views here.


def question_list(request):
    return render(request, 'questions/question_list.html', {})


def question_detail(request, question_id):
    return render(request, 'questions/question_detail.html', {})