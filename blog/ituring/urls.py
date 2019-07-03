from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='ituring'),
    path('book/', views.book, name='book'),
    path('article/', views.article, name='article'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('about/', views.AboutView.as_view()),
]
