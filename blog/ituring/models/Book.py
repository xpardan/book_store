from django.contrib.auth.models import User
from django.db import models


class BookCategory(models.Model):
    """
    图书分类
    """
    cate_name = models.CharField(max_length=100)


class BookTag(models.Model):
    """
    图书标签
    """
    tag_name = models.CharField(max_length=100)


class Book(models.Model):
    """
    图书基本资料
    """
    # 基本信息
    name = models.CharField(max_length=255)  # 图书名称
    thumbnail = models.ImageField()  # 图书预览图
    cover = models.ImageField()  # 图书大封面图
    author = models.ManyToManyField(User, related_name='author')  # 图书作者
    translator = models.ManyToManyField(User, related_name='translator')  # 图书译者
    status = models.IntegerField()  # 图书状态 (正在印刷，正在排版)
    tags = models.ManyToManyField(BookTag)  # 图书标签
    description = models.TextField()  # 描述

    # 出版信息
    book_category_name = models.ForeignKey(BookCategory, on_delete=models.CASCADE)  # 系列书名
    editor = models.ForeignKey(User, on_delete=models.CASCADE)  # 编辑er
    publish_date = models.DateTimeField()  # 出版日期
    ISBN = models.CharField(max_length=191)  # 图书编号
    pages = models.IntegerField()  # 页数
    print_mode = models.CharField(max_length=191)  # 印刷模式
    book_size = models.CharField(max_length=191)  # 开本
    publish_status = models.CharField(max_length=191)  # 出版状态
    origin_name = models.CharField(max_length=191)  # 书籍原名
    origin_ISBN = models.CharField(max_length=191)  # 原书号

    # 价格
    cost_price = models.DecimalField(decimal_places=2, max_digits=12)  # 进价
    market_price = models.DecimalField(decimal_places=2, max_digits=12)  # 市场价
    discount_price = models.DecimalField(decimal_places=2, max_digits=12)  # 折扣价
