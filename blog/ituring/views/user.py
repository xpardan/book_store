from django.shortcuts import render
from django.views.generic import TemplateView


def register(request):
    return render(request, 'ituring/user/register.html', {'title_name': '新用户注册'})


def login(request):
    return render(request, 'ituring/user/login.html', {'title_name': '新用户注册'})


class AboutView(TemplateView):
    template_name = 'ituring/about.html'
