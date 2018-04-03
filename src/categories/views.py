from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Category
import urllib.parse
from django.views.generic import CreateView
from .forms import CategoryForm, CategoryListForm


def category_list(request):
    categories = Category.objects.all()
    category_form = CategoryForm(request.POST)
    search_form = CategoryListForm(request.GET)
    if search_form.is_valid():
        data = search_form.cleaned_data
        if data['sort']:
            categories = categories.order_by(data['sort'])
        if data['search']:
            categories = categories.filter(name__icontains=data['search'])
    if category_form.is_valid():
        data = category_form.cleaned_data
        category = Category.objects.create(name=data['name'])
        category.save()
    context = {
        'categories': categories,
        'category_form': category_form,
        'search_form': search_form,
    }

    return render(request, 'categories/category_list.html', context)


def category_detail(request, pk=None):
    category = get_object_or_404(Category, name=urllib.parse.unquote(pk))
    context = {
        'category': category,
        'questions': category.questions.all(),
        'id': category.id,
    }
    return render(request, 'categories/category_detail.html', context)


