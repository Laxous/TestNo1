from django.contrib import admin
from index.models import *
# Register your models here.

# 把制定数据模型添加到admin后台，方法一
admin.site.register(ActionApi)

# 方法二
@admin.register(userinfo)
class ActionApiAdmin(admin.ModelAdmin):
	# 设置显示字段
	list_display = ['id','name','moblie_no','address',]