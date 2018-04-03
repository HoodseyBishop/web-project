from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from .models import Question, Answer
from questions.forms import QuestionListForm, AnswerForm
from django.views import View
from django.views.generic import UpdateView, CreateView, ListView


def question_list(request):
    questions = Question.objects.all().filter(is_archive=False)
    form = QuestionListForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        if data['sort']:
            questions = questions.order_by(data['sort'])
        if data['search']:
            questions = questions.filter(title__icontains=data['search'])
    context = {
        'questions': questions,
        'questions_form': form,
    }
    return render(request, 'questions/question_list.html', context)


class QuestionEdit(UpdateView):
    model = Question
    fields = 'title', 'text', 'categories',
    template_name = 'questions/question_edit.html'

    def get_queryset(self):
        queryset = super(QuestionEdit, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

    def get_success_url(self):
        return reverse('question_detail', kwargs={'pk': self.object.pk})


class QuestionCreate(CreateView):
    model = Question
    fields = 'title', 'text', 'categories',
    template_name = 'questions/question_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(QuestionCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('question_detail', kwargs={'pk': self.object.pk})


def question_detail(request, pk=None):
    question = get_object_or_404(Question, pk=pk)
    form = AnswerForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        answer = Answer.objects.create(
            text=data['text'],
            question=Question.objects.get(pk=pk),
            author=request.user
        )
        answer.author = request.user
        answer.save()
    context = {
        'question': question,
        'answers': question.answers.all().filter(is_archive=False),
        'categories': question.categories.all(),
        'form': form,
    }
    return render(request, 'questions/question_detail.html', context)

