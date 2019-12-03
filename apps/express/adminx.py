import xadmin
from .models import *


class KdNiaoExpressConfigAdmin(object):
    pass


class ExpressCompanyAdmin(object):
    pass


class OrderExpressAdmin(object):
    pass


xadmin.site.register(KdNiaoExpressConfig, KdNiaoExpressConfigAdmin)
xadmin.site.register(ExpressCompany, ExpressCompanyAdmin)
xadmin.site.register(OrderExpress, OrderExpressAdmin)