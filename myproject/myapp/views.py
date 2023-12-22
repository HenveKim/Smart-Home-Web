from django.shortcuts import render,HttpResponse,redirect
from myapp.models import *
from django import forms
from myapp.utils.encrypt import md5

#ModelForm
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password',"email","phonenumber"]
    # clean_字段名
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        # return什么.password字段保存什么
        return md5(pwd)

    # 钩子函数
    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm_password")
        if md5(confirm) != pwd:
            raise forms.ValidationError("密码不一致!")
        
        # return返回什么,字段 confirm_password 保存至数据库的值就是什么
        return md5(confirm)
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','phonenumber']
class UserResetModelForm(forms.ModelForm):

    confirm_password = forms.CharField(
        label = "确认密码",
        widget = forms.PasswordInput(render_value=True),
    )

    class Meta:
        model = User
        fields = ["password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    # clean_字段名
    def clean_password(self):
        pwd = self.cleaned_data.get("password")

        # 校验当前数据库中的密码与用户输入的新密码是否一致
        exists = User.objects.filter(uid=self.instance.pk, password=md5(pwd))
        if exists:
            raise forms.ValidationError("密码不能与当前密码一致!")

        # return什么.password字段保存什么
        return md5(pwd)

    # 钩子函数
    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm_password")
        if md5(confirm) != pwd:
            raise forms.ValidationError("密码不一致!")
        
        # return返回什么,字段 confirm_password 保存至数据库的值就是什么
        return md5(confirm)
class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "userName"}),
        required=True,
    )
    password = forms.CharField(
        label="用户名",
        # render_value=True 表示当提交后,如果密码输入错误,不会自动清空密码输入框的内容
        widget=forms.PasswordInput(attrs={"class": "password"}, ),
        required=True,
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['rno','name','num']
class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = ['fno','name','state','room']
class FurnitureEditForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = ['name','state','room']

# Create your views here.

def index(request):
    #return HttpResponse("欢迎")
    #检查是否登录
    # info = request.session.get("info")
    # if not info:
    #     return redirect("/login/")

    return render(request, 'index.html')
def registbk(request):
        if request.method == "GET":
            return render(request, 'registbk.html')
        #获取用户提交的数据
        uid = request.POST.get("username")
        password = request.POST.get("password")
        account = request.POST.get("rename")
        phonenumber = request.POST.get("telphone")
        # 添加到数据库
        a=User.objects.create(uid=uid, password=password, account=account, phonenumber=phonenumber)
        return redirect('/login/')
def regist(request):
     #ModelForm
    if request.method == "GET": 
        form = UserForm()
        return render(request, "regist.html", {"form":form})
    
    # 用户POST请求提交数据,需要进行数据校验
    form = UserForm(data=request.POST)
    if form.is_valid():
        #print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/login/")
    else:
        # 校验失败(在页面上显示错误信息)
        return render(request, "regist.html", {"form":form})
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
        #网站生成随机字符串,写到用户浏览器的cookie中,再写入到服务器的session中
        request.session['info'] = {'uid':User_object.uid,'username':User_object.username,'email':User_object.email,'phonenumber':User_object.phonenumber}
        return redirect('/index/')

    return render(request, 'login.html',{'form':form})
def logout(request):

    """ 注销 """

    # 清楚当前session
    request.session.clear()

    return redirect("/login/")
def homeworkstay(request):
    form = Room.objects.all().order_by("rno")
    return render(request, 'homeworkstay.html',{"form":form})
def homeworkstayin(request,no):
    form = Furniture.objects.filter(room_id=no)
    return render(request, 'homeworkstayin.html',{"form":form})
# def wode1(request):
#     return render(request, 'wode1.html')
def useredit(request):
    info_dict = request.session.get('info')
    id = info_dict.get('uid')
    row_object = User.objects.filter(uid=id).first()
    if not row_object:
        return redirect('/wode1/')

    if request.method == "GET":
        form = UserEditForm(instance=row_object)
        return render(request, "wode1change.html", {"form": form})

    form = UserEditForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/wode1/')
    
    return render(request, "wode1change.html", {"form": form})
def userreset(request):
    """重置密码"""

    # 判断 id 是否存在
    info_dict = request.session.get('info')
    id = info_dict.get('uid')
    
    row_object = User.objects.filter(uid=id).first()
    if not row_object:
        return redirect('/wode1/')

    if request.method == "GET":
        form = UserResetModelForm(instance=row_object)
        
        return render(request, "wode1.html", {"form": form})

    form = UserResetModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/wode1/")

    return render(request, "wode1.html", {"form": form})

def scene(request):
    return render(request, 'scene.html')

def roomadd(request):
    """添加房间"""
    if request.method == "GET":
        form = RoomForm()
        return render(request, "homeworkstaychange.html", {"form": form})

    # 用户POST请求提交数据,需要进行数据校验
    form = RoomForm(data=request.POST)
    if form.is_valid():
        #print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/homeworkstay/")
    
    # 校验失败(在页面上显示错误信息)
    return render(request, "homeworkstaychange.html", {"form": form})

def furnitureadd(request):
    """添加家具"""
    if request.method == "GET":
        form = FurnitureForm()
        return render(request, "homeworkstayinchange.html", {"form": form})

    # 用户POST请求提交数据,需要进行数据校验
    form = FurnitureForm(data=request.POST)
    if form.is_valid():
        #print(form.cleaned_data)
        # 直接保存至数据库
        form.save()
        return redirect("/homeworkstay/")
    
    # 校验失败(在页面上显示错误信息)
    return render(request, "homeworkstayinchange.html", {"form": form})

def Furnitureedit(request,nid):
    # 判断 id 是否存在
    row_object = Furniture.objects.filter(fno=nid).first()
    if not row_object:
        return redirect('/homeworkstay/')

    if request.method == "GET":
        form = FurnitureEditForm(instance=row_object)
        return render(request, "homeworkstayinchange.html", {"form": form})

    form = FurnitureEditForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/homeworkstay/')
    
    return render(request, "homeworkstayinchange.html", {"form": form})
def Furnituredelete(request,nid):
    Furniture.objects.filter(fno=nid).delete()
    return redirect("/homeworkstay/")
