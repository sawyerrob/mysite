from django.shortcuts import render
import time,datetime
from .models import User
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
		somebody = request.POST.get('somebody')
		motion = request.POST.get('dept')
		message = request.POST.get('message')
		gender = request.POST.get('gender')
		avatar = request.FILES.get('avatar')

		# 此处获得ip地址，如果是有代理或者本机，则默认不会获取到127.0.0.1
			# if request.META.has_key('HTTP_X_FORWARDED_FOR'):
			# 	ip = request.META['HTTP_X_FORWARDED_FOR']
			# else:
			# 	ip = request.META['REMOTE_ADDR']
		# ip = request.META['HTTP_X_FORWARDED_FOR']

		# 此处写入头像到静态文件夹
		with open('anonymous/media/icon/'+avatar.name, 'wb') as f:

			for chunk in avatar.chunks():

				f.write(chunk)

		# 此处拼接一个日期的字符串
		current_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
		time_list =current_time.split('-')
		date_date =time_list[0]+"-"+time_list[1]+'-'+time_list[2]
		date_date2 = datetime.datetime.now()

		# 此处更新到数据库
		obj = User(nickname=nickname, somebody=somebody,motion=motion,message=message,gender=gender,avatar=avatar,date1=date_date2)
		obj.save()

		data = {
					nickname:nickname,
					somebody:somebody,
					motion:motion,
					message:message,
					gender:gender,
					avatar:avatar,

		}


		return render(request,'anonymous/elements.html',{'data':data})