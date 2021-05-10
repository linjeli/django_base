from django.apps import AppConfig


class BookConfig(AppConfig):
    name = 'book'
    verbose_name = '书籍管理'   # 修改后台显示的表名，在settings配置中使用方案2注册类名
