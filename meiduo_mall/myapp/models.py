from django.db import models


# Create your models here.
class Greades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)


class Students(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField()
    sage = models.IntegerField(default=True)
    scontent = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    # 关联外键
    sgrade = models.ForeignKey("Grades")
