from django.shortcuts import render, HttpResponse


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
