from django.db import models
from django.utils import timezone
from apps.order.models import OrderInfo


class KdNiaoExpressConfig(models.Model):
    appId = models.CharField(default='', max_length=128, verbose_name='APP ID')
    appKey = models.CharField(default='', max_length=128, verbose_name='APP KEY')
    isProd = models.BooleanField(default=True, verbose_name='催单')

    class Meta:
        db_table = 'gd_kdniao_config'
        verbose_name = '快递鸟配置'
        verbose_name_plural = verbose_name


class ExpressCompany(models.Model):
    name = models.CharField(default='未命名快递公司', max_length=128, verbose_name='快递公司名称')
    code = models.CharField(default='', max_length=64, verbose_name='快递公司编码')

    class Meta:
        db_table = 'gd_express_company'
        verbose_name = '快递公司'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class OrderExpress(models.Model):
    express_status = (
        (0, '未发货'),
        (1, '已发货'),
        (2, '已收件')
    )
    order = models.OneToOneField(OrderInfo, related_name='order', on_delete=models.CASCADE, verbose_name='订单')
    company = models.ForeignKey(ExpressCompany, related_name='company', null=True,
                                on_delete=models.SET_NULL, verbose_name='快递公司')
    expressId = models.CharField(default='', max_length=128, verbose_name='订单编号')
    expressStatus = models.SmallIntegerField(default=0, choices=express_status, verbose_name='快递状态')
    expressInfo = models.TextField(default=None, null=True, blank=True, verbose_name='快递信息')
    expressInfoUpdateTime = models.DateTimeField(default=timezone.now(), null=True, blank=True, verbose_name='快递信息更新时间')

    class Meta:
        db_table = 'gd_order_express'
        verbose_name = '快递信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}-{}-{}'.format(self.order.id, self.order.name, self.express_status[self.expressStatus][1])





