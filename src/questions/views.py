from django.http import HttpResponseForbidden
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from .models import Question, Answer
from questions.forms import QuestionListForm, AnswerCreateForm
from django.views import View
from django.views.generic import UpdateView, CreateView, ListView, DetailView
from likes.models import Like
from django.views.generic.detail import SingleObjectMixin
from django.db import models


class QuestionList(ListView):
    model = Question
    queryset = Question.objects.order_by('-created')
    template_name = 'questions/question_list.html'
    context_object_name = 'questions'

    def get_queryset(self):
        questions = super(QuestionList, self).get_queryset().filter(is_archive=False)
        request = self.request
        form = QuestionListForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            if data['sort']:
                questions = questions.order_by(data['sort'])
            if data['search']:
                questions = questions.filter(title__icontains=data['search'])
        return questions.prefetch_related('categories').select_related('author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(QuestionList, self).get_context_data()
        context['question_form'] = QuestionListForm(self.request.GET)
        return context


class QuestionEdit(UpdateView):
    model = Question
    fields = 'title', 'text', 'categories',
    template_name = 'questions/question_edit.html'

    def get_queryset(self):
        queryset = super(QuestionEdit, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        print(queryset)
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

    if request.method == 'POST':
        if request.user.is_anonymous:
            raise HttpResponseForbidden
        form = AnswerCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            answer = Answer.objects.create(
                text=data['text'],
                question=Question.objects.get(pk=pk),
                author=request.user
            )
            answer.author = request.user
            answer.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = AnswerCreateForm()
    context = {
        'question': question,
        'answers': question.answers.all().filter(is_archive=False),
        'categories': question.categories.all(),
        'answer_form': form,
    }
    return render(request, 'questions/question_detail.html', context)


class AnswerCreate(CreateView):
    model = Answer
    fields = 'text',
    template_name = 'questions/answer_create.html'
    context_object_name = 'answer_form'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AnswerCreate, self).form_valid()


class QuestionLikeView(View):
    def dispatch(self, request, pk=None, *args, **kwargs):
        self.question_object = get_object_or_404(Question, id=pk)
        return super(QuestionLikeView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        like = self.question_object.likes.filter(author=request.user).first()
        if like is None:
            like = Like()
            like.author = request.user
            like.question = self.question_object
            Question.objects.all().filter(id=self.question_object.id).update(like_count=models.F('like_count') + 1)
            like.save()
        else:
            like.delete()
            Question.objects.all().filter(id=self.question_object.id).update(like_count=models.F('like_count') - 1)
        return HttpResponse(Like.objects.filter(question=self.question_object).count())


class AnswerView(DetailView):
    queryset = Question.objects.all()
    template_name = 'questions/question_answers.html'

# class QuestionDetail(DetailView):
#     model = Question
#     template_name = 'questions/question_detail.html'
#
#     def get_queryset(self):
#         request = self.request
#         if request.method == 'POST' and not request.user.is_anonymous:
#             form = AnswerCreateForm(request.POST)
#             if form.is_valid():
#                 data = form.cleaned_data
#                 answer = Answer.objects.create(
#                     text=data['text'],
#                     question=Question.objects.get(pk=self.model.pk),
#                     author=request.user
#                 )
#                 answer.save()
#         return super(QuestionDetail, self).get_queryset()
#
#     def get_context_data(self, **kwargs):
#         context = super(QuestionDetail, self).get_context_data()
#         question = kwargs['object']
#         context['answer_form'] = AnswerCreateForm(self.request.POST)
#         context['answers'] = question.answers.all().filter(is_archive=False)
#         context['categories'] = question.categories.all()
#         return context
