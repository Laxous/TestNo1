from django.shortcuts import render

# Create your views here.
def index(request):
	info={"title":"首页",'list':[1,2,3,4,5,6,7,'jfj','fke'],'name':'anges','ppp':1111}
	return render(request, 'index1.html', info)

def tests(request):
	info={"title":"首页",'list':[1,2,3,4,5,6,7,'jfj','fke'],'name':'anges','ppp':1111}
	return render(request, 'index.html',info)
