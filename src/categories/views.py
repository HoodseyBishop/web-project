from django.shortcuts import render, HttpResponse

# Create your views here.


def category_list(request):
    context = {}
    context['categories'] = [
        {'id': '1', 'name': 'category #1'},
        {'id': '2', 'name': 'category #2'},
        {'id': '3', 'name': 'category #3'},
    ]

    return render(request, 'categories/category_list.html', context)


def category_detail(request, pk = None):
    context = {}
    context['category'] = {
        'name': 'category 1',
        'id': pk
    }

    return render(request, 'categories/category_detail.html', context)