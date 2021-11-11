# -*- coding: utf-8 -*-
__author__ = 'pengweijian'

from rest_framework import serializers
from api import models


class CategoryViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ArticleViewSerializers(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField(required=False)

    class Meta:
        model = models.Article
        fields = '__all__'

    def get_comments(self, obj):
        return obj.comment_set.all().values('id','content').distinct()
        # return [tag for tag in obj.tags.all().values('name').distinct()]


class CommentViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'
