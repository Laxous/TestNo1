# -*- coding: utf-8 -*-

def add(*a):
	print(a)
	print(type(a))
	if a is not None:
		p = []
		for i in a:
			p.append(i)
		print(p)

# add(1,4,6,8,2)

# 1.不定长参数，可以不写
# 2.不定长参数，传入函数或方法里面，默认为元组类型

def foo(**a):   # 默认类型为字典 dict
	print(a)
	print(type(a))
foo(name='mengmeng',a=1,b=3,h=888,o='name')
