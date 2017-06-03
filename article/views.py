# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime

# Create your views here.
def home(request): #定义一个名为home的处理请求的函数
    return HttpResponse("Hello, World, Django")  #返回字符串"Hello, World, Django"

def detail(request, my_args):
    post = Article.objects.all()[int(my_args)] #查询所有结果，并进行索引，索引值为my_args
    #格式化字符串元组
    str = ("title = %s, category = %s, date_time = %s, content = %s" % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)

def home(request):
    post_list = Article.objects.all() #查询Article的所有结果，赋给post_list变量
    #render()结合一个给定的模板和上下文字典，返回一个渲染后的HttpResponse对象，两个必选参数request(用于生成request)和template_name（模板名称），第三个参数是字典类型的可选参数
    return render(request, 'home.html', {'post_list': post_list}) 

