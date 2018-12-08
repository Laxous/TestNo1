from django.test import TestCase
# Create your tests here.
import time
"""
	%Y  四位数的年份表示
    %m  月份
    %d  月内中的一天
    %H  24小时制小时数
    %M  分钟数
    %S  秒
    %z  Time zone offset from UTC.
    %a  本地简化星期名称
    %A  本地完整星期名称
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  12小时制小时数
    %p  Locale's equivalent of either AM or PM.
    不仅仅局限与这些格式，其他格式可以去其他文档查看
"""
t = time.time() # 当前时间的时间戳
a = time.localtime(t) # 时间戳，转换为时间元组
b = time.strftime("%Y-%m-%d %H:%M:%S",a)  # 格式化日期
c = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
print(c)
