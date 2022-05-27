from django.shortcuts import redirect, render, HttpResponse

from app01.models import UserInfo


# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")


def user_list(request):
    name = "yctang"
    roles = ["学生", "老师", "家长"]
    user_info = {"name": "yctang", "salary": 100, "role": "11"}
    # 去 app 目录下的templates目录寻找user_list.html（根据app的注册顺序，逐一去它们的templates目录寻找）
    return render(request, "user_list.html", {'n1': name, 'n2': roles, 'n3': user_info})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        print(request.POST)
        return HttpResponse("登录成功")


def info_list(request):
    # 1. 获取数据库中所有用户信息
    data_list = UserInfo.objects.all()

    print(data_list)

    return render(request, "info_list.html", {'info_list': data_list})


def info_add(request):
    if request.method == 'GET':
        return render(request, 'info_add.html')
    elif request.method == 'POST':
        user = request.POST.get("user")
        password = request.POST.get("pwd")
        age = request.POST.get("age")

        UserInfo.objects.create(name=user, password=password, age=age)

        return redirect("/info/list")


def info_del(request):
    nid = request.GET.get('id')
    UserInfo.objects.filter(id = nid).delete()
    return redirect("/info/list")
