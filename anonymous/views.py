from django.shortcuts import render
import time
from django.http import HttpResponse
from django.template import loader
def index(request):
	return render(request,'anonymous/index.html')
# Create your views here.
def elements(request):
	if request == 'GET':
		return render(request,'anonymous/elements.html')
	else:
		nickname = request.POST.get('name')
		somobody = request.POST.get('somebody')
		motion = request.POST.get('dept')
		message = request.POST.get('message')
		current_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
		time_list =current_time.split('-')
		year=time_list[0]
		month=time_list[1]
		day =time_list[2]
		print(nickname,somobody,motion,message,year,month,day)
		return render(request,'anonymous/elements.html')