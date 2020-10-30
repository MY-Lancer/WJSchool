from django.db import models
from django.contrib.auth.models import AbstractUser

# 用户信息
class User(AbstractUser):

    # 电话号码字段
    # unique 为唯一性字段
    mobile = models.CharField(max_length=20, unique=True,blank=True)

    # 学院信息
    # 
    userName = models.CharField(max_length=20,db_column='Name')#用户名称
    # 学院

    userCollege = models.CharField(max_length=20,db_column='College')#用户名称
    # 修改认证的字段
    USERNAME_FIELD = 'mobile'

    #创建超级管理员的需要必须输入的字段
    REQUIRED_FIELDS = ['username','email']

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        db_table='tb_user'              #修改默认的表名
        verbose_name='用户信息'         # Admin后台显示
        verbose_name_plural=verbose_name # Admin后台显示

    def __str__(self):
        return self.mobile
