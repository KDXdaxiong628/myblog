from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import models


# Create your views here.
# 获取文章列表
def index(request):
    #  get(pk=1)-----获取主键为1的表
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

# 获取文章详情
def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})

# 文章编辑
def edit_page(request, article_id):
    # 判断是不是新建文章
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    # 不是新建文章
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})

# 提交文章
def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')

    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        # 返回主页
        return HttpResponseRedirect('/blog/index')
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    # 返回原先的博客详情页-
    return HttpResponseRedirect('/blog/article/%s' % str(article.id))  #render(request, 'blog/article_page.html', {'article': article})