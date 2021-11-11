from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
from api import serializer
from django.core.exceptions import ObjectDoesNotExist
import datetime
import time

from rest_framework.pagination import PageNumberPagination


class CategoryView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            if pk:
                category = models.Category.objects.get(id=pk)
                articles = category.article_set.all()
                page_objects = PageNumberPagination()
                result = page_objects.paginate_queryset(articles, request, self)
                print(result)
                ser = serializer.ArticleViewSerializers(instance=result, many=True)
                if ser.data:
                    return page_objects.get_paginated_response(ser.data)
                # return Response(ser.data)
                else:
                    return Response("页码id不存在")
            else:
                return Response('请指定目录id')
        except ObjectDoesNotExist:
            return Response('该目录不存在')

    def post(self, request, *args, **kwargs):
        ser = serializer.CategoryViewSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            if pk:
                category = models.Category.objects.get(id=pk)
                articles = category.article_set.all()
                if not articles:
                    category.delete()
                    return Response('目录删除成功')
                else:
                    return Response('该目录为非空目录，无法删除')
            else:
                return Response('请指定目录id')
        except ObjectDoesNotExist:
            return Response('对象不存在')


class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            print(pk)
            if pk:
                articles = models.Article.objects.get(id=pk)
                ser = serializer.ArticleViewSerializers(instance=articles)
            else:
                articles = models.Article.objects.all()
                ser = serializer.ArticleViewSerializers(instance=articles, many=True)

            return Response(ser.data)
        except ObjectDoesNotExist:
            return Response('文章不存在')

    def post(self, request, *args, **kwargs):
        ser = serializer.ArticleViewSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)

    def put(self, request, *args, **kwargs):
        """全部更新"""
        try:
            pk = kwargs.get('pk')
            if pk:
                article_object = models.Article.objects.get(id=pk)
                # 关键字参数 instance ；如果提供了，则 save() 会更新这个实例。如果没有，则 save() 会创建一个对应模型的新实例
                ser = serializer.ArticleViewSerializers(instance=article_object, data=request.data)
                if ser.is_valid():
                    ser.save()
                    return Response(ser.data)
                else:
                    return Response(ser.errors)
            else:
                return Response('请指定文章id')
        except ObjectDoesNotExist:
            return Response('对象不存在')

    def delete(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            print(pk)
            if pk:
                articles = models.Article.objects.get(id=pk)
                articles.delete()
                return Response('文章删除成功')
            else:
                return Response("请指定文章id")

        except ObjectDoesNotExist:
            return Response('对象不存在')


class CommentView(APIView):
    def get(self, request, *args, **kwargs):
        article_id = request.GET.get('article_id')
        try:
            article = models.Article.objects.get(id=article_id)
            comments = article.comment_set.all()
            ser = serializer.CommentViewSerializers(instance=comments, many=True)
            if ser:
                return Response(ser.data)
            else:
                return Response('该文章暂无评论')
        except ObjectDoesNotExist:
            return Response('文章不存在')

    def post(self, request, *args, **kwargs):
        ser = serializer.CommentViewSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else:
            return Response(ser.errors)
