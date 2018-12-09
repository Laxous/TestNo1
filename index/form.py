# -*- coding: utf-8 -*-
from django import forms
from .models import *

class CaseTypeForm(forms.Form):
	# 文本框
	descriptions = forms.CharField(max_length=50,label='描述')
	# 下拉框
	choices_list = [(i+1,v['type_name']) for i,v in enumerate(CaseType.objects.values('type_name'))]
	type = forms.ChoiceField(choices=choices_list,label='用例类型')
	# forms.BooleanField 复选框
	# forms.DateField 文本框，具有验证日期格式的功能
	# forms.EmailField 验证输入是否是合法的邮箱地址
	# 共同参数
	# Label 用于生成label标签，或者显示内容
	# Initial 设置初始值
	# help_text 设置帮助提示信息
	# error_messages 设置错误信息。以字典格式表示
	# Disabled 是否可以编辑
	# required 输入数据是否为空，默认值就是True
	# Widget 设置HTML控件的样式


