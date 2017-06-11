# Django-blog
项目目的
通过动手做项目，可以大概了解开发的工作内容，找工作也相对容易一些。

项目名称
Django搭建简易博客

项目背景
本项目介绍如何一步步使用Django开发一个简单的博客Web应用，适用于有Python和Django基础的同学。项目时间：6.1-6.7

项目内容
第1节 开发环境以及项目与App
第2节 Models和Admin以及Views和URL
第3节 Template和动态URL
第4节 Markdown和代码高亮
第5节 归档，AboutMe和标签分类
第6节 搜索和Readmore以及RSS和分页

涉及知识（技术栈）
Django框架及Web开发、MVC、Template

MVC：一种软件架构模式，把软件系统分为三个部分：Model（模型）、View（视图）、Controller（控制）
1、	View：最上面的一层，是直接面向最终用户的“视图层“。它是提供给用户的操作界面，是程序的外壳
2、	Controller：中间的一层，就是“控制层”，它负责根据用户从“视图层”输入的指令，选取“数据层”中的数据，然后对其进行相应的操作，产生最终的结果
3、	Model：最底下的一层，是核心的“数据层”，也就是程序需要操作的数据和信息
（在Django中，采用MTV架构，即Model、Template、View，对应MVC架构中的Model、View、Controller，原理相同，只是取名不同。）

Django工作原理：用户在浏览器输入URL后的回车，浏览器会对URL进行检查，首先判断协议，如果是http就按照Web来处理，然后调用DNS查询，将域名转换为IP地址，然后经过网络传输到达对应Web服务器，服务器对url进行解析后，调用View中的逻辑（MTV中的V），其中又设计到Model（MTV中的M），与数据库进行交互，将数据发送到Template（MTV中的T）进行渲染，然后发送到浏览器中，浏览器以合适的方式呈现给用户

