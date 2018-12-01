from django.db import models

# models.AutoField 默认生成一个自增长的字段，类型为int
# models.CharField 字符串类型
# models.BooleanField 布尔类型
# models.CommaSeparatedIntegerField 用逗号分割的整数类型
# models.DateField 日期data
# models.DateTimeField 日期datatime
# models.Decimal 十进制小数类型
# models.EmailField 字符串类型，正则表达式邮箱
# models.FloatField 浮点型
# models.IntegerField 整型
# models.BigIntegerField 长整型
# models.TextField 长文本类型

# Create your models here.
class userinfo(models.Model):
	# id，自增长的整数，primary_key用来定义主键，一个数据表只有一个主键
	id=models.AutoField(primary_key=True)
	name=models.CharField(null=False,db_index=True,max_length=50)    # 字符串类型，不为空，添加数据库索引
	moblie_no=models.CharField(max_length=20,null=True)   # 整型，可以为空
	address=models.TextField(max_length=200,null=True)
	created_at=models.DateTimeField(auto_now_add=True)  # 只在创建/添加的时候，更新的时间
	updated_at = models.DateTimeField(auto_now=True)  # 每次更新都可以更新的时间
	des=models.TextField(max_length=200,null=True)
	abanding_flag=models.IntegerField(default=1)  # 整型，默认值为1

class ActionApi(models.Model):
	"""接口管理页面数据表"""
	id = models.AutoField(primary_key=True)
	action_name = models.CharField(max_length=50)
	api_path = models.CharField(max_length=50)
	params = models.TextField(max_length=200)
	headers = models.TextField(max_length=200)
	abandon_flag = models.IntegerField(default=1) # 1有效 0删除
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	created_by = models.CharField(max_length=20)
	updated_by = models.CharField(max_length=20)
	descriptions = models.TextField(max_length=200)

