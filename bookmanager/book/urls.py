# -*- coding = utf-8 -*-
# Author：凌杰
# Email：577709198@qq.com

from django.urls import path
from book import views


# 这是固定写法 urlpatterns
urlpatterns = [
    # path(路由，视图函数名)
    path('', views.index),
    path('index/', views.index),
]