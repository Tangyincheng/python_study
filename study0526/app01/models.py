from django.db import models


# Create your models here.
class Department(models.Model):
    title = models.CharField(verbose_name="标题", max_length=32)


class UserInfo(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(
        verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")

    # 1.约束
    # - to 与哪张表关联
    # - to_filed 表中的哪一列关联
    # 2.django自动
    # - 写的depart
    # - 生成数据列 depart_id
    # 3.部门表被删除
    # 3.1 级联删除
    depart = models.ForeignKey(
        to="Department", to_field="id", on_delete=models.CASCADE)
    # 3.2 置空
    # depart = models.ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)

    # 在django中做的约束
    gender_choices = (
        (1, '男'),
        (2, '女')
    )

    gender = models.SmallIntegerField(
        verbose_name='性别', choices=gender_choices)
