# -*- coding = utf-8 -*-
# Author：凌杰
# Email：577709198@qq.com
from django.urls import path
from book.views import index

urlpatterns = [
    path('index/', index),
]