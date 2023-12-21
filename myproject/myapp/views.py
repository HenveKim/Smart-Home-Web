from django.shortcuts import render,HttpResponse,redirect
from myapp.models import *
from django import forms


#ModelForm
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        #fields = "__all__"
        fields = ['username','password',"email","phonenumber"]

class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )
    password = forms.CharField(
        label="用户名",
        # render_value=True 表示当提交后,如果密码输入错误,不会自动清空密码输入框的内容
        widget=forms.PasswordInput(attrs={"class": "form-control"}, ),
        required=True,
    )

# Create your views here.



def index(request):
    #return HttpResponse("欢迎")
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
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
def regist2(request):
     #ModelForm
    if request.method == "GET": 
        form = UserForm()
        return render(request, "regist2.html", {"form":form})
    
    # 用户POST请求提交数据,需要进行数据校验
    form = UserForm(data=request.POST)
    if form.is_valid():
        #print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/login/")
    
    # 校验失败(在页面上显示错误信息)
    return render(request, "regist2.html", {"form":form})

def login(request):
    """登录"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html',{'form':form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        #验证成功,获取到的用户名和密码
        #print(form.cleaned_data)

        # 去数据库校验用户名和密码是否正确
        User_object = User.objects.filter(username=form.cleaned_data['username'], password=form.cleaned_data['password']).first()
        if not User_object:
            form.add_error("password","用户名或密码错误")
            return render(request, 'login.html', {'form': form})

        #用户名和密码输入正确
        return redirect('/index/')

    return render(request, 'login.html',{'form':form})