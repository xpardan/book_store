from django.contrib.auth.models import User
from django.db import models
from .Book import Book


class Comment(models.Model):
    """
    评论
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=191)
    publish_date = models.DateTimeField()
    recommend_times = models.IntegerField()
