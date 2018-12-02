from django.shortcuts import render
from index.models import *
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def index(request):
	info={"title":"首页",'list':[1,2,3,4,5,6,7,'jfj','fke'],'name':'anges','ppp':1111}
	return render(request, 'index1.html', info)

@login_required(login_url='/login/')
def tests(request):
	info={"title":"首页"}
	list =[{'name':'空空','age':18},{'name':'咸鱼','age':20}]
	a=userinfo.objects.all()
	info['iiii']=a
	info['infolist']=list
	return render(request, 'index.html',info,status=200)

def login_index(request):
	return render(request, 'login.html')

def signin(request):
	"""登录接口"""
	if request.method=='POST':
		username = request.POST.get('userid')
		password = request.POST.get('psw')
		if User.objects.filter(username=username):  # 通过User模型，判断用户名是否已注册
			user = auth.authenticate(username=username,password=password)
			if user:
				if user.is_active:
					login(request,user)
				return HttpResponseRedirect('/test/',locals())  # 登录成功之后，重定向到页面
				# locals 自动把定义的变量组合成dict传输
			else:
				tips = '账号密码错误，请重新输入'
				return render(request,'login.html',locals())
		else:
			tips = '用户不存在，请先注册'
			return render(request, 'login.html', locals())

@login_required(login_url='/login/')
def action_index(request):
	"""接口列表"""
	info = {
		'action_list':ActionApi.objects.all(),
		'username':request.user.username,
		'name':request.user.first_name + request.user.last_name
	}
	return render(request, "action_api/action_index.html", info)

@login_required(login_url='/login/')
def action_add(request):
	"""添加接口"""
	return render(request, "action_api/action_add.html")

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
		a = ActionApi.objects.get(id=info['id'])
		a.action_name = info['apiname']
		a.api_path = info['apipath']
		a.params = info['params']
		a.headers = info['headers']
		a.abandon_flag = info['status']
		a.updated_by = request.user.username
		a.save()
		return JsonResponse({'status':200})