from django.shortcuts import render, redirect
from web import models


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
