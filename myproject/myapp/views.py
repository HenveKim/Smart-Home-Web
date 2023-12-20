from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("欢迎")
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def homeworkstay(request):
    return render(request, 'homeworkstay.html')
def homeworkmake(request):
    return render(request, 'homeworkmake.html')