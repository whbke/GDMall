# from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models

from common.base_model import BaseModel


class AppConfig(BaseModel):
    '''
    APP配置
    '''
    minOrderAmount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='起送额度')
    freeFreight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='免运费额度')
    freightAmount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='运费')
    isOpen = models.BooleanField(default=True, verbose_name='是否开业')
    closeDesc = models.CharField(max_length=1024, blank=True, verbose_name='观点说明')
    appId = models.CharField(max_length=128, blank=True, verbose_name='APP ID')
    appSecret = models.CharField(max_length=128, blank=True, verbose_name='APP Secret')
    mchId = models.CharField(max_length=128, blank=True, verbose_name='MCH ID')
    mchKey = models.CharField(max_length=128, blank=True, verbose_name='MCH KEY')
    emailSender = models.CharField(max_length=128, blank=True, verbose_name='发送邮箱账户')
    emailSenderPassword = models.CharField(max_length=128, blank=True, verbose_name='发送邮箱密码')
    emailReceivers = models.CharField(max_length=512, blank=True, verbose_name='接受邮箱，使用","分开')
    sslSendSMTPServer = models.CharField(max_length=512, blank=True, verbose_name='发送邮箱SMTP_SSL服务器地址')
    sslSendSMTPServerPort = models.IntegerField(default=465, blank=True, verbose_name='发送邮箱SMTP_SSL服务器端口')

    class Meta:
        db_table = 'gd_app_config'
        verbose_name = 'APP配置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)


class User(BaseModel, AbstractUser):
    '''
    用户信息模型
    '''
    birthday = models.CharField(max_length=50, blank=True, verbose_name='出生日期')
    height = models.CharField(max_length=30,default=0, blank=True, verbose_name='身高')
    weight = models.CharField(max_length=30,default=0, blank=True, verbose_name='体重')
    phone = models.CharField(max_length=11, default=0, verbose_name='手机号码')

    class Meta:
        db_table = 'gd_user'
        verbose_name = '员工信息'
        verbose_name_plural = verbose_name


class WxUser(BaseModel):
    '''
    用户信息模型
    '''
    open_id = models.CharField(max_length=50, verbose_name='用户openid')
    nick_name = models.CharField(max_length=30, default='未命名用户', verbose_name='昵称')
    head_portrait = models.CharField(max_length=255, default='未上传头像', verbose_name='用户头像')
    birthday = models.CharField(max_length=30, default='', verbose_name='出生日期')
    height = models.CharField(max_length=10, default='', verbose_name='身高')
    weight = models.CharField(max_length=10, default='', verbose_name='体重')
    phone = models.CharField(max_length=11, default=0, verbose_name='手机号码')
    integral = models.IntegerField(default=0, verbose_name='会员积分')
    is_active = models.BooleanField(default=1,verbose_name='是否激活')

    class Meta:
        db_table = 'gd_wx_user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class Address(BaseModel):
    '''
    用户收货地址
    '''
    wx_user = models.ForeignKey(WxUser,on_delete=models.CASCADE,verbose_name='微信用户')
    name = models.CharField(max_length=30, verbose_name='收件人')
    phone = models.CharField(max_length=11, null=True, verbose_name='联系人电话')
    address = models.CharField(max_length=255, verbose_name='收件地址')
    address_code = models.CharField(max_length=10,default='',verbose_name='邮编号')
    is_default = models.BooleanField(default=0, verbose_name='是否默认')

    class Meta:
        db_table = 'gd_address'
        verbose_name = '收货地址信息'
        verbose_name_plural = verbose_name


class VipLevel(BaseModel):
    '''
    会员等级
    '''
    level = models.CharField(max_length=20, verbose_name='等级名称')
    minmum_integral = models.IntegerField(verbose_name='积分要求值')

    class Meta:
        db_table = 'gd_vip_level'
        verbose_name = '会员等级'
        verbose_name_plural = verbose_name

