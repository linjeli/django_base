from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo


# Create your views here.


def index(request):
    # 在这里实现增删改查
    books = BookInfo.objects.all()
    return HttpResponse(books)

# name = 'abc'
# mysql 的数据储存在 硬盘
# redis 的数据储存在 内存
# 把硬盘的数据保存在内存 也称之为 缓存


# 增加数据
# 方式一：在 python3 manage.py shell 里面添加
from book.models import BookInfo

book = BookInfo(
    name='Django',
    pub_date='2000-1-1',
    readcount=10
)
# 必须要调用对象的save方法才能将数据保存到数据库中
book.save()

# 方式2：objects -- 相当于一个代理 实现增删改查
BookInfo.objects.create(
    name='测试开发入门',
    pub_date='2020-1-1',
    readcount=100
)

# 修改数据
# 方式一：
# select * from bookinfo where id=6
book = BookInfo.objects.get(id=6)
book.name = '运维开发入门'
# 想要保存数据，也是需要调用对象的save方法
book.save()

# 方式二：
# filter 过滤
BookInfo.objects.filter(id=6).update(name='爬虫入门', commentcount=666)

# 错误的，get方法后面没有update
# BookInfo.objects.get(id=5).update(name='555', commentcount=999)


# 删除数据
# 方式一：
book = BookInfo.objects.get(id=6)

# 删除分2种，物理删除（这条记录的数据删除） 和 逻辑删除（修改标记位 例如 is_delete=False）
book.delete()

# 方式二：
BookInfo.objects.get(id=5).delete()
BookInfo.objects.filter(id=5).delete()

# 查询数据
# get 查询单一结果，如果不存在会抛出模型类.DoesNotExist异常
try:
    book = BookInfo.objects.get(id=1)
except BookInfo.DoesNotExist:
    print('查询结果不存在')

# all 查询多个结果
BookInfo.objects.all()
from book.models import PeopleInfo

PeopleInfo.objects.all()

# count 查询结果数量
BookInfo.objects.all().count()
# 或者
BookInfo.objects.count()

# 过滤查询
# 实现SQL中的where功能，包括
# filter 过滤出多个结果
# exclude 排除符合条件剩下的结果
# get 过滤单一结果

# 语法形式：
# 模型类名.objects.filter(属性名__运算符=值)       获取n个结果  n=0,1,2,...
# 模型类名.objects.exclude(属性名__运算符=值)      获取n个结果  n=0,1,2,...
# 模型类名.objects.get(属性名__运算符=值)          获取1个结果 或者 异常


# 查询编号为1的图书
book = BookInfo.objects.get(id=1)  # 简写形式（属性名=值）
book = BookInfo.objects.get(id__exact=1)  # 完整形式（id__exact=1）

BookInfo.objects.get(pk=1)  # pk primary key 主键

BookInfo.objects.get(id=1)  # get 得到的是一个
BookInfo.objects.filter(id=1)  # filter得到的是 列表

# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')  # contains 包含

# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')  # endswith 结尾

# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)  # __isnull=True 为空值

# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1, 3, 4])

# 查询编号大于3的图书
# 大于 gt         great 大
# 大于等于 gte     equal 等于
# 小于 lt         less then 或者 litte
# 小于等于 lte
BookInfo.objects.filter(id__gt=3)

# 查询编号不等于3的书籍
BookInfo.objects.exclude(id=3)

# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)

# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')
BookInfo.objects.filter(pub_date__gt='1990-01-01')
# BookInfo.objects.filter(pub_date__gt='19900101')    # 错误日期写法


# F和Q对象
# F 对象，两个属性比较
from django.db.models import F

# 使用：2个属性的比较
# 语法形式： 以filter为例  模型类名.objects.filter(属性名__运算符=F('第二个属性名'))

# 查询阅读量大于等于评论量的图书
BookInfo.objects.filter(readcount__gte=F('commentcount'))

# 查询阅读量大于等于2倍评论量的图书
BookInfo.objects.filter(readcount__gte=F('commentcount') * 2)

# 并且查询
# 查询阅读量大于20，并且编号小于3的图书
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
# 或者
BookInfo.objects.filter(readcount__gt=20, id__lt=3)

# 或者查询
# 查询阅读量大于20，或者编号小于3的图书
from django.db.models import Q

# 或者语法：模型类名.objects.filter(Q(属性名__运算符=值)|Q(属性名__运算符=值)|...)
# 并且语法：模型类名.objects.filter(Q(属性名__运算符=值)&Q(属性名__运算符=值)&...)
# not 非 语法： 模型类名.objects.filter(~Q(属性名__运算符=值))
BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lt=3))

# 查询编号不等于3的图书
BookInfo.objects.exclude(id=3)
# 或者
BookInfo.objects.filter(~Q(id=3))


# 聚合函数 Sum求和，Max求最大值，Min求最小值，Avg求组中值的平均值,Count求数量
from django.db.models import Sum, Max, Min, Avg, Count
# 模型类名.objects.aggregate(Xxx('字段名'))
BookInfo.objects.aggregate(Sum('readcount'))


# 排序
BookInfo.objects.all().order_by('readcount')    # 升序
BookInfo.objects.all().order_by('-readcount')    # 降序


# 2个表的级联操作

# 查询书籍为1的所有人物信息
book = BookInfo.objects.get(id=1)
book.peopleinfo_set.all()

# 查询人物为1的书籍信息
person = PeopleInfo.objects.get(id=1)
person.book.name
person.book.readcount


# 关联过滤查询

# 语法形式
# 查询1的数据，条件为 n
# 模型类名.objects.(关联模型类名小写__字段名__运算符=值)

# 查询图书，要求图书人物为"郭靖"
BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
# 可以用简约写法
BookInfo.objects.filter(peopleinfo__name='郭靖')

# 查询图书，要求图书中人物的描述包含"八"
BookInfo.objects.filter(peopleinfo__description__contains='八')  # contains 包含


# 查询书名为"天龙八部"的所有人物
PeopleInfo.objects.filter(book__name='天龙八部')

# 查询图书阅读量大于30的所有人物
PeopleInfo.objects.filter(book__readcount__gt=30)

