from django.shortcuts import render
from index.models import *
# Create your views here.
def index(request):
	info={"title":"首页",'list':[1,2,3,4,5,6,7,'jfj','fke'],'name':'anges','ppp':1111}
	return render(request, 'index1.html', info)

def tests(request):
	info={"title":"首页"}
	list =[{'name':'空空','age':18},{'name':'咸鱼','age':20}]
	a=userinfo.objects.all()
	info['iiii']=a
	info['infolist']=list
	return render(request, 'index.html',info,status=200)
