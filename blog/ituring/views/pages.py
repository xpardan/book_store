from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    html = """
    <h1>Hello</h1>
    """
    return HttpResponse(html)


def index(request):
    return render(request, 'ituring/home/home.html', {'title_name': '首页'})


def article(request):
    return render(request, 'ituring/article/index.html', {'title_name': '文章'})


def book(request):
    return render(request, 'ituring/book/index.html', {'title_name': '图书'})


def search(request):
    pass
