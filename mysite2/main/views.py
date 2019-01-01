from django.shortcuts import render
import json
from users.models import User
from tool_03.models import Blog,Comment
from django.http import HttpResponse
from tool_03.models import Comment
from tool_03.forms import CommentForm
import datetime
from main import aaa
# Create your views here.
def index(request):
	a=Blog.objects.all().order_by('-id')[:5]
	aaa.speak()
	return render(request,'basemain.html',{'blogs':a})

def article(request,id):
	a=Blog.objects.get(id=id)
	b=Comment.objects.filter(blog_id=id)
	return render(request, 'wenzhang.html',{'blog':a,'all_comment':b})

def comment(request):
	request.encoding = 'utf-8'
	if request.method=='GET':
		c=Comment.objects.create(blog_id=request.GET.get('blog_id'), user_name=request.GET.get('user_name'),
							   content=request.GET.get('comment'), create_at=datetime.datetime.now())
		a = Blog.objects.get(id=request.GET.get('blog_id'))

		b=Comment.objects.filter(blog_id=request.GET.get('blog_id'))
		os.system('ilang "网友%s在你的文章%s中留言，%s"'%(request.GET.get('user_name'),a.name,c.content))
		return render(request, 'wenzhang.html', {'blog': a, 'all_comment': b})


def accounts_profile(request):
	if request.method=='POST':
		a=json.loads(request.body)
		print(a)
		b=User.objects.get(email=request.user.email)
		b.name=a['name']
		b.sex=a['sex']
		b.graduate_time=a['graduate_time']
		b.id_number=a['id_number']
		b.job=a['job']
		b.job_2=a['job_2']
		b.job_join_time=a['job_join_time']
		b.job_number=a['job_number']
		b.job_time=a['job_time']
		b.phone=a['phone']
		b.school=a['school']
		b.sex=a['sex']
		b.team_belong=a['team_belong']
		b.xue_li=a['xue_li']
		b.zhengzhi_miaomao=a['zhengzhi_miaomao']
		b.zhengzhi_time=a['zhengzhi_time']
	
		b.save()
	return render(request,'accounts_profile.html')