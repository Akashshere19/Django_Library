from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(BookRecord)
class BookRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'BookName', 'OutDate', 'InDate','UserName','MobNo')
