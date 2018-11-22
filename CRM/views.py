from django.shortcuts import render,HttpResponse,redirect
from CRM import models

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get("pwd")
        user = models.User.objects.filter(user=username,pwd=pwd).first()
        if user:
            request.session['user'] = user.user
            roles = user.roles.all()
            url_list = roles.values("permissions__url","permissions__code","permissions__title").distinct()
            url_tem =[]
            menu_list = []
            for url in url_list:
                url_tem.append(url["permissions__url"])
                if url["permissions__code"] == "list":
                    menu_list.append({
                        "title":url["permissions__title"],
                        "url":url["permissions__url"],
                    })
            request.session["permissions__url"] = url_tem
            request.session["permissions__menu_list"] = menu_list
            return redirect('/index/')


    return render(request,"login.html")


def index(request):


    return render(request,"stark/index.html")