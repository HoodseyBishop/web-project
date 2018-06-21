from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import HttpResponseForbidden, Http404
from .models import Category
import urllib.parse
from django.shortcuts import reverse
from django.views.generic import CreateView, ListView
from .forms import CategoryForm, CategoryListForm


class CategoryCreate(CreateView):
    model = Category
    fields = 'name',

    def get_success_url(self):
        return reverse('category_list')


class CategoryList(ListView):
    model = Category
    queryset = Category.objects.all().order_by('name')
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        categories = super(CategoryList, self).get_queryset()
        form = CategoryListForm(self.request.GET)
        if form.is_valid():
            data = form.cleaned_data
            if data['sort']:
                categories = categories.order_by(data['sort'])
            if data['search']:
                categories = categories.filter(name__icontains=data['search'])
        # return categories.annotate(question_count=models.Count('questions__id'))
        return categories.aggregate_questions()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['category_form'] = CategoryForm(self.request.POST)
        context['search_form'] = CategoryListForm(self.request.GET)
        return context


class CategoryListCreate(CategoryCreate, CategoryList):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'


def category_list(request):
    categories = Category.objects.all()
    search_form = CategoryListForm()
    category_form = CategoryForm()
    if request.method == 'GET':
        search_form = CategoryListForm(request.GET)
        if search_form.is_valid():
            data = search_form.cleaned_data
            if data['sort']:
                categories = categories.order_by(data['sort'])
            if data['search']:
                categories = categories.filter(name__icontains=data['search'])
    elif request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            data = category_form.cleaned_data
            category = Category.objects.create(name=data['name'])
            category.save()
        return redirect('category_list')
    context = {
        'categories': categories,
        'category_form': category_form,
        'search_form': search_form,
    }

    return render(request, 'categories/category_list.html', context)


def category_detail(request, pk=None):
    category = get_object_or_404(Category, pk=pk)
    context = {
        'category': category,
        'questions': category.questions.all(),
        'id': category.pk,
    }
    return render(request, 'categories/category_detail.html', context)


