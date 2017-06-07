# -*- coding: utf-8 -*-
import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()  #为了成为一个可用的标签库，这个模块必须包含一个名为register的变量，它是template.Library的一个实例，所有的标签和过滤器都是在其中注册的
#register.filter()是一个装饰器，相当于custom_markdown=resigter.filter(customer_markdown)
@register.filter(is_safe=True)  #进行注册，把写好的自定义过滤器函数custom_markdown注册为你的Library实例，is_safe=True表示此过滤器没有引入任何HTML不安全字符（<、>、‘、’或$）到结果中
@stringfilter  #在对象传入你的函数之前把这个对象转换给它的字符串值
def custom_markdown(value):
	#mark_safe()为了HTML的输入，明确的标记字符串为安全
    return mark_safe(markdown.markdown(value,
        extensions = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'],
                                       safe_mode=True,
                                       enable_attributes=False))
