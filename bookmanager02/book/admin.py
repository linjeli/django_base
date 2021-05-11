from django.contrib import admin
from book.models import BookInfo, PeopleInfo
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date', 'readcount', 'commentcount', )


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'description')


admin.site.register(BookInfo, BookAdmin)
admin.site.register(PeopleInfo, PeopleAdmin)
