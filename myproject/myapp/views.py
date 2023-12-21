from django.shortcuts import render,HttpResponse,redirect
from myapp.models import *
# Create your views here.

def index(request):
    #return HttpResponse("欢迎")
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def regist(request):
    return render(request, 'regist.html')
def homeworkstay(request):
    return render(request, 'homeworkstay.html')
def homeworkmake(request):
    return render(request, 'homeworkmake.html')
def regist(request):
        if request.method == "GET":
            return render(request, 'regist.html')
        #获取用户提交的数据
        uid = request.POST.get("username")
        password = request.POST.get("password")
        account = request.POST.get("rename")
        phonenumber = request.POST.get("telphone")
        # 添加到数据库
        a=User.objects.create(uid=uid, password=password, account=account, phonenumber=phonenumber)
        return redirect('/login/')