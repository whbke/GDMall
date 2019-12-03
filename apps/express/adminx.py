import xadmin
from .models import *


class KdNiaoExpressConfigAdmin(object):
    pass


class ExpressCompanyAdmin(object):
    pass


class OrderExpressAdmin(object):
    fields = ['id', 'order', 'company', 'expressId', 'expressStatus']
    list_display = ['id', 'order', 'company', 'expressId', 'expressStatus']


xadmin.site.register(KdNiaoExpressConfig, KdNiaoExpressConfigAdmin)
xadmin.site.register(ExpressCompany, ExpressCompanyAdmin)
xadmin.site.register(OrderExpress, OrderExpressAdmin)