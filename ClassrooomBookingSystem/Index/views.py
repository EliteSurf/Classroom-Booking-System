from django.shortcuts import render


def index_page(request):
    return render(request, 'Index/Index.html', {'title': 'Index'})
