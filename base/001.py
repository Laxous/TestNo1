# -*- coding: utf-8 -*-

print("hello"+"django")
a = "hello django"
b = "mmmm"
print(a+" django")
print("%s django %s"%(a,b) )
# 这是一个单行注释
"""
这是一个多行注释
"""
'''
这也是一个多行注释
'''
# python中，单引号和双引号，交替使用
c = 27843728974923
print(type(c))
print(type(b))

print(a[2]) # 索引从0开始计算

# 列表定义
l1 = [1,6,3,12,9654,23,0]
l2 = ['f','e','c','o','uo']
l1.append(78)  # 往列表中添加元素
print(l2.pop(2))  # 输入index，返回移除的内容
print(l2)
print(l2.remove('e'))  # 输入移除内容，返回值为空
print(l2)
l1.sort()
print(l1)

t1 = (1,6,3,12,9654,23,0)
t2 = ('f','e','c','o','uo')
# 元组，可以理解为一个锁定的列表
print(t2.count('o'))

d1 = {'name':'梦梦',
      'aaa':1111,
      'bbb':'fdsjf'}
# 字典中的数据，成对存在，字典无序，字典中的key，有唯一性
d1.pop('name')
# d1.clear()
print(d1)
d1['ccc']='cxzcxz'
print(d1)
print(d1.keys())
print(d1.values())
