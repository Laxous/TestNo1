# -*- coding: utf-8 -*-
import random
a = 2
num = random.randint(0,100)
count = 1
while 10>count>0:
	if a==num:
		print("猜对了")
		break
	elif 0<a<num:
		print("猜小了")
		count+=1
		continue
	elif 100>a>num:
		print("猜大了")
		count += 1
		continue
	else:
		print("数字不在范围内")