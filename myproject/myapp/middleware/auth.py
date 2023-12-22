from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect

class AuthMiddleware(MiddlewareMixin):
    
    def process_request(self, request):
        #排除无需登录即可访问页面
        if request.path_info == "/login/" :
            return None
        if request.path_info == "/regist/" :
            return None
        # 判断用户是否登录
        info_dict = request.session.get('info')
        if info_dict:
            return None
        else:
            # 跳转到登录页面
            return redirect('/login/')