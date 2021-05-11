from django.db import models

# Create your models here.

"""
1. 模型类，需要继承自 models.Models
2. 定义属性
    - id属性默认会生成
    - 属性名 = models.类型(选项)
    - 属性名对应就是字段名
    - 属性名不要使用python/mysql关键字，也不要使用连续的下划线 __
    - 类型：mysql的类型
    - 选项：是否有默认值，是否唯一，是否为null
        - CharField 必须设置 max_length
        - verbose_name 主要是 admin 站点使用
3. 改变表的名称
    - 默认表的名称是：子应用名_类名，都是小写
    - 修改表的名字

create table 'qq_user' (
    id init,
    name verchar(10) not null default ''
)
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name='名字')     # unique=True 唯一性
    pub_date = models.DateField(null=True, verbose_name='发布日期')
    readcount = models.IntegerField(default=0, verbose_name='阅读数')
    commentcount = models.IntegerField(default=0, verbose_name='评论数')
    is_delete = models.BooleanField(default=False)

    # 1对多的关系模型中
    # 系统会自动为我们自动添加一个 关联模型类名小写_set
    # propleinfo_set=[PeopleInfo,PeopleInfo...]

    class Meta:
        db_table = 'bookinfo'   # 修改表的名字
        verbose_name = '书籍管理'     # admin站点使用的
        verbose_name_plural = '书籍管理'

    # Python 3 直接定义 __str__() 方法即可，系统使用这个方法来把对象转换成字符串
    def __str__(self):
        return self.name


class PeopleInfo(models.Model):

    # 定义一个有序字典
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )

    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1, verbose_name='性别')    # choices选择,设置默认值
    description = models.CharField(max_length=100, null=True, verbose_name='描述')
    is_delete = models.BooleanField(default=False)

    # 外键
    # 系统会自动为外键添加 _id

    # 外键的级联操作
    # 主表 和 从表
    # 1   对  多
    # 书籍 对 人物

    # 主表的一条书籍如果删除了
    # 从表有关联的数据怎么办呢
    # SET_NULL 为空
    # 抛出异常，不让删除
    # 级联删除

    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '角色人物'  # admin站点使用的
        verbose_name_plural = '角色人物'

    # Python 3 直接定义 __str__() 方法即可，系统使用这个方法来把对象转换成字符串
    def __str__(self):
        return self.name