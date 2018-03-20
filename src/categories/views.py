from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Category


def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }

    return render(request, 'categories/category_list.html', context)


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    context = {
        'category': category,
        'questions': category.questions.all()
    }

    return render(request, 'categories/category_detail.html', context)