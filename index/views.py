from django.shortcuts import render
from index.models import *
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import *
from django.views.decorators.csrf import csrf_exempt
import logging
# Create your views here.
logger = logging.getLogger('index.app')

@csrf_exempt
def index(request):
	info={"title":"首页",'list':[1,2,3,4,5,6,7,'jfj','fke'],'name':'anges','ppp':1111}
	return render(request, 'index1.html', info)

@login_required(login_url='/login/')
def tests(request):
	logger.info('进入首页')
	info={"title":"首页"}
	list =[{'name':'空空','age':18},{'name':'咸鱼','age':20}]
	logger.info('获取列表信息'+str(list))   # info打的日志，内容，都是字符串类型。
	a=userinfo.objects.all()
	info['iiii']=a
	info['infolist']=list
	return render(request, 'index.html',info,status=200)

def login_index(request):
	logger.info('进入登录页面')
	return render(request, 'login.html')

def signin(request):
	"""登录接口"""
	if request.method=='POST':
		username = request.POST.get('userid')
		password = request.POST.get('psw')
		logger.info('登录用户名：'+ str(username))
		logger.info('登录密码：'+ str(password))
		if User.objects.filter(username=username):  # 通过User模型，判断用户名是否已注册
			logger.info('用户已注册，开始登录')
			user = auth.authenticate(username=username,password=password)
			if user:
				if user.is_active:
					login(request,user)
					logger.info('登录成功，跳转主页')
				return HttpResponseRedirect('/test/',locals())  # 登录成功之后，重定向到页面
				# locals 自动把定义的变量组合成dict传输
			else:
				tips = '账号密码错误，请重新输入'
				logger.info(tips)
				return render(request,'login.html',locals())
		else:
			tips = '用户不存在，请先注册'
			logger.info(tips)
			return render(request, 'login.html', locals())

@login_required(login_url='/login/')
def action_index(request):
	"""接口列表"""
	info = {
		"title": "首页",
		'action_list':ActionApi.objects.all(),
		'username':request.user.username,
		'name':request.user.first_name + request.user.last_name
	}
	logger.info('进入接口列表')
	return render(request, "action_api/action_index.html", info)

@login_required(login_url='/login/')
def action_add(request):
	"""添加接口"""
	info = {
		"title": "首页",
	}
	return render(request, "action_api/action_add.html",info)

def send_api(request):
	"""添加接口信息的接口"""
	if request.method == "POST":
		info = request.POST
		# 添加数据到数据表
		a = ActionApi()
		a.action_name = info['apiname']
		a.api_path = info['apipath']
		a.params = info['params']
		a.headers = info['headers']
		a.abandon_flag = 1  # 可加，可不加
		a.created_by = request.user.username
		a.updated_by = request.user.username
		a.save()
		return JsonResponse({'status':200})

def updata_api(request):
	"""更新接口信息的接口"""
	if request.method == "POST":
		info = request.POST
		# 更新数据到数据表
		action_id = str(info['id']).strip()
		a = ActionApi.objects.get(id=int(action_id))
		a.action_name = str(info['apiname']).strip()
		a.api_path = str(info['apipath']).strip()
		a.params = str(info['params']).strip()
		a.headers = str(info['headers']).strip()
		a.abandon_flag = str(info['status']).strip()
		a.updated_by = request.user.username
		a.save()
		return JsonResponse({'status': 200})
