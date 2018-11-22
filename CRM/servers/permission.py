
from django.shortcuts import HttpResponse,render,redirect
import re
from django.utils.deprecation import MiddlewareMixin

class PermissionMiddleware(MiddlewareMixin):

    def process_request(self,request):

        current_path=request.path
        print(current_path)

        # 白名单
        white_url=["/login/","/index/"]
        for reg in white_url:
            ret=re.search(reg,current_path)
            if ret:
                return None

        # 校验用户是否登录
        user=request.session.get("user")
        if not user:
            return redirect("/login/")

        # 权限认证
        permission_list=request.session.get("permissions__url")
        print(permission_list)
        for reg in permission_list:
            reg="^%s$"%reg
            ret=re.search(reg,current_path)
            print('ret',ret)
            if ret:
                return None
        return HttpResponse("无权限访问！")