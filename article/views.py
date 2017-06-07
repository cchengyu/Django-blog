# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.syndication.views import Feed

# Create your views here.
class RSSFeed(Feed): #定义一个名为RSSFeed的类，继承Feed。Feed是一个高等级的聚合框架，用来创造RSS
        title = "RSS feed -article" #对应RSS的<title>，用于前端显示的标题
        link = "feeds/posts/" #对应RSS的<link>，用于Feed的当前位置绝对路径
        description = "RSS feed -blog posts" #对应RSS的<description>，用于前端显示的描述

        def items(self): #定义一个名为items的函数
                return Article.objects.order_by('-date_time') #返回所有对象按照时间倒序排序的列表

        def item_title(self, item): #定义一个名为item_title的函数，传入参数item
                return item.title #返回项的标题

        def item_pubdate(self, item):
                return item.date_time #返回项的日期时间

        def item_description(self, item):
                return item.content #返回项的内容

def home(request):
        posts = Article.objects.all() #查询所有的Article对象赋给posts
        paginator = Paginator(posts, 2) #每页显示两个，传入对象的列表和每一个分配的元素数量，Paginator会进行分页
        page = request.GET.get('page') #查找GET数据里键为page的值（这里是页码）赋给page变量，get()为字典的get()方法，用来得到指定键的值，
        try:
                post_list = paginator.page(page) #获取在提供的下标处的Page对象，下标以1开始
        except PageNotAnInteger : #当向page()提供一个不是整数的值时（即page不是整数）抛出这个异常
                post_list = paginator.page(1) #获取下标处为1的Page对象
        except EmptyPage : #当向page()提供一个有效值，但是那个页面上没有任何对象时抛出
                post_list = paginator.page(paginator.num_pages) #获取最后一页对象，paginator.num_pages表示页面总数，
        return render(request, 'home.html', {'post_list': post_list})

def detail(request, id): #传入request和id参数
        try: #使用try的错误处理机制
            post = Article.objects.get(id=str(id)) #查询id值为str(id)的Article对象，赋给post变量
        except Article.DoesNotExist: #执行try的代码出错时，跳转这里，如果Article对象不存在
            raise Http404 #跑出django定义的404错误
        #render()结合一个给定的模板和上下文字典，返回一个渲染后的HttpResponse对>象，两个必选参数request(用于生成request)和template_name（模板名称），第三个参数>是字典类型的可选参数
        return render(request, 'post.html', {'post': post})
def archives(request):
        try:
                post_list = Article.objects.all()
        except Article.DoesNotExist:
                raise Http404
        return render(request, 'archives.html', {'post_list': post_list, 'error':False})

def about_me(request):
    return render(request, 'aboutme.html')

def search_tag(request,tag):
    try:
        post_list = Article.objects.filter(category = tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list':post_list})
def blog_search(request):
    if 's' in request.GET: #如果用户输入的表单在GET数据里
        s = request.GET['s'] #把GET数据里名为s的字段赋给变量s
        if not s: #if s is not None，如果s为空
                return render(request, 'home.html') #返回主页
        else: #如果s不为空
                post_list = Article.objects.filter(title__icontains = s) #过滤出标题含有s的Article对象，icontains是不区分大小写的模糊匹配
                if len(post_list) == 0: #如果匹配结果为空
                        return render(request,'archives.html', {'post_list': post_list, 'error': True}) #返回archive.html页面，传递错误给模板
                else:
                        return render(request,'archives.html', {'post_list': post_list, 'error': False})#返回archive.html页面
    return redirect('/') #重定向到主页

