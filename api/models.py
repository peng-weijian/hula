from django.db import models

# Create your models here.
from django.db import models
import datetime


class Category(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name='目录名称', max_length=20)


class Tag(models.Model):
    tag = models.CharField(verbose_name='标签', max_length=20)


class Article(models.Model):
    status_choices = (
        (1, '已发布'),
        (0, '未发布')
    )

    # 对于非动态变化的字段，可以不用foreignkey单独分表出来，直接用下面的方式，choice会被加载到内存，查询速度快
    # 对于动态变化的字段，则使用foreignkey单独分表出来

    status = models.IntegerField(verbose_name='发布状态', choices=status_choices, default=1)
    create_time = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)

    category = models.ForeignKey(verbose_name='所属栏目', to=Category, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='文章标题', max_length=30)
    content = models.TextField(verbose_name='文章内容', max_length=2000)
    page_view = models.IntegerField(verbose_name='浏览量', default=0)
    tag = models.ManyToManyField(verbose_name='标签', to=Tag, default=None)


class Comment(models.Model):
    create_time = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    article = models.ForeignKey(verbose_name='目标文章', to=Article, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='文章内容', max_length=2000)
