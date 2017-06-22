# -*- coding= utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Article(models.Model): #定义一个名为Article的类，从父类models.Model继承，拥>有父类的全部功能
         #定义博客题目，调用models中的CharField方法，用来存储字符串类型字段，max_length设置最大长度为100，赋给title变量
        title = models.CharField(max_length = 100)
        #定义博客标签，最大长度为50，blank表示空白属性，True表示这个字段允许为空白，其他同理
        category = models.CharField(max_length = 50, blank = True)
        #定义博客日期，DateTimeField用于存储日期类型字段，auto_now_add表示对象第一次被创建时自动设置为当前时间，用于创建时间的时间戳，即取文章初次创建的时间，这里设置为True
        date_time = models.DateTimeField(auto_now_add = True)
        #定义博客正文，TextField用于存储文本类型字段，允许为空白，null=True表示在>数据库中将存储空值，即无数据
        content = models.TextField(blank = True, null = True)
     #获取URL并转换成url的表示格式
        def get_absolute_url(self):
            path = reverse('detail', kwargs={'id':self.id}) #reverse用来反解析url以访问其他视图方法，'detail'是要使用的view方法，kwargs={'id':self.id}是传入方法的参数
            return "http://116.62.106.233:80%s" % path #返回url
        #python2使用__unicode__, python3使用__str__
        #定义一个__str__函数，用来创建Article对象的字符串表示形式，一般系统默认使>用<Atricle:Article object>来表示对象，通过这个函数可以告诉系统使用字符串来表示这个对象
        def __str__(self):
                return self.title #返回字符串self.title

        class Meta: #按时间下降排序
                ordering = ['-date_time'] #

