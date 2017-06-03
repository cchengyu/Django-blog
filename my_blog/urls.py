# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from article import views #从article中导入views模块
#patterns()用来存储url和处理逻辑的关系列表，接受前缀（这里为空）和任意数量的URL>模式，并返回Django需要的格式的URL模式列表，
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
        #url()用来关联url和处理逻辑的关系，必选参数为regex(正则表达式)和view
        #r'^admin/'是正则表达式，r''是正则表达式的格式，^表示行的开头，^admin/表示行的开头必须是admin/
        #r'^$'是正则表达式，$表示行的结束，^$表示匹配到空的字符串
        #include()接受python完整的导入路径，返回应该包括在这个地方的URLconf模块>，方便Django调用
    url(r'^admin/', include(admin.site.urls)),
    #(?P<name>...)表示把...中匹配到的内容传给name，name作为参数传给后面的函数，^表示行的开头必须为括号中的内容，\d可以匹配一个数字，+表示至少一个字符，\d+表示匹配至少一个数字，/$表示以/结尾
#这里表示将传入的一位或者多位数字作为参数传递到views中的detail作为参数
#name用来命名URL，使URL可以在Django的其他地方使用，特别是在模板中
    url(r'^(?P<my_args>\d+)/$', views.detail, name='detail'),
    url(r'^$', views.home),
)
