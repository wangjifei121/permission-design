from django.db import models


class User(models.Model):
    user=models.CharField(max_length=32,verbose_name='姓名')
    pwd=models.CharField(max_length=32,verbose_name="密码")
    roles=models.ManyToManyField("Role",verbose_name="职位")

    def __str__(self):
        return self.user


class Role(models.Model):
    title=models.CharField(max_length=32,verbose_name="职位")
    permissions=models.ManyToManyField("Permission")

    def __str__(self):
        return self.title


class Permission(models.Model):
    url=models.CharField(max_length=128)
    title = models.CharField(max_length=32,verbose_name="权限名称")
    code=models.CharField(max_length=32,default="list")
    def __str__(self):
        return self.title