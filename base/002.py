# -*- coding: utf-8 -*-

b = 1  # 从定义的哪一行开始，往下的所有行数，都有效
class people:
	def __init__(self,m):  # 初始化方法
		self.o = b + 3
		self.qwe = m  # 类的属性
	def add(self,a):   # 类的方法  cls
		# print(a)
		self.c = 1
		print(self.qwe)
		return a
	@classmethod   # 类方法
	def aoo(cls):
		d = b-2
		return d
	@staticmethod   # 静态方法
	def boo():
		print(11111)

p = people('name')  # 类的实例化，p就是类的实例化对象
print(p.qwe)
print(p.add(9))
print(p.aoo())
print(people.aoo())
people.boo()
p.boo()
# self 类的实例化