from django.shortcuts import render

# Create your views here.
"""
视图，就是python函数
视图函数有2个要求：
    1. 视图函数的第一个参数就是接收请求
    2. 必须返回一个响应
"""
# request
from django.http import HttpRequest
from django.http import HttpResponse

# 我们期望用户输入 http://127.0.0.1:8000/index/
# 来访问视图函数


def index(request):

    # return HttpResponse('OK')
    # render    渲染模板
    # request   请求
    # template_name   模板名字

    # context=None  上下文，理解为将视图中的数据传递给HTML，HTML采用{{ 字典的key }}来展示数据
    # 模拟数据查询
    context = {
        'name': '马上双11，点击有惊喜'
    }
    return render(request, 'book/index.html', context=context)