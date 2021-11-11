"""hula URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 文章接口
    re_path('^articles/(?P<pk>\d+)$', views.ArticleView.as_view()),
    re_path('articles', views.ArticleView.as_view()),
    # 分类接口
    re_path('^category/(?P<pk>\d+)$', views.CategoryView.as_view()),
    re_path('category', views.CategoryView.as_view()),

    # 评论接口
    re_path('^comment/(?P<article_id>\d+)$', views.CommentView.as_view()),
    re_path('comment', views.CommentView.as_view()),
]
