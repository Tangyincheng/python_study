from django.shortcuts import render, redirect, HttpResponse
from web import models
from django import forms


# Create your views here.
def depart_list(request):
    queryset = models.Department.objects.all()

    return render(request, "depart_list.html", {"queryset": queryset})


def depart_add(request):
    if request.method == "GET":
        return render(request, "depart_add.html")
    elif request.method == "POST":
        title = request.POST.get("title")
        models.Department.objects.create(title=title)
        return redirect('/depart/list/')


def depart_delete(request):
    nid = request.GET.get("nid")
    models.Department.objects.filter(id=nid).delete()
    return redirect('/depart/list/')


def depart_edit(request, nid):
    if request.method == 'GET':
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request, "depart_edit.html", {'row_object': row_object})
    elif request.method == 'POST':
        title = request.POST.get('title')
        models.Department.objects.filter(id=nid).update(title=title)
        return redirect('/depart/list/')


def user_list(request):
    # 用户列表
    queryset = models.UserInfo.objects.all()

    # for obj in queryset:
    #     print(obj.id, obj.name, obj.account, obj.create_time.strftime("%Y-%m-%d"), obj.gender, obj.get_gender_display(), obj.depart_id, obj.depart.title)

    return render(request, 'user_list.html', {"queryset": queryset})


def user_add(request):
    if request.method == 'GET':
        context = {
            'gender_choices': models.UserInfo.gender_choices,
            'depart_list': models.Department.objects.all()
        }
        return render(request, 'user_add.html', context)
    elif request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        age = request.POST.get('age')
        account = request.POST.get('ac')
        ctime = request.POST.get('ctime')
        gender = request.POST.get('gd')
        depart_id = request.POST.get('dp')

        models.UserInfo.objects.create(name=user, password=pwd, age=age, account=account, create_time=ctime,
                                       gender=gender,
                                       depart_id=depart_id)

        return redirect('/user/list/')


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", 'gender', 'depart']
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "password": forms.TextInput(attrs={'class': 'form-control'}),
            "age": forms.TextInput(attrs={'class': 'form-control'}),
        }


def user_model_form_add(request):
    print("111")
    form = UserModelForm()
    return render(request, "user_model_form_add.html", {'form': form})
