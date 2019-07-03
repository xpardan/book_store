from django.shortcuts import render


def register(request):
    return render(request, 'ituring/user/register.html', {'title_name': '新用户注册'})


def login(request):
    return render(request, 'ituring/user/login.html', {'title_name': '新用户注册'})
