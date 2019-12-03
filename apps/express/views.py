import json

from django.utils import timezone

from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
from apps.order.models import OrderInfo
from apps.user.models import WxUser
from common.express_utils import get_express_info
from common.public_function import PublicFunction

from .models import *
from .serializers import *


class OrderExpressView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        order_info_id = data['order_info_id']
        token = data['token']

        # 参数校验
        if not all([token, order_info_id]):
            return Response({'msg': '数据不完整'})
        # 获取用户open_id
        open_id = PublicFunction().getOpenIdByToken(token)
        # 校验用户
        if open_id:
            try:
                wx_user = WxUser.objects.get(open_id=open_id)
            except:
                return Response({'msg': '用户不存在'})
            try:
                order_info = OrderInfo.objects.get(pk=order_info_id)
            except:
                return Response({'msg': '订单不存在'})
            try:
                order_express = OrderExpress.objects.get(order=order_info)
            except:
                order_express = OrderExpress.objects.create(order=order_info)
                order_express.save()

            express_info = None
            if order_express.expressStatus == 1:
                need_update = False
                if not order_express.expressInfo \
                    or order_express.expressInfoUpdateTime is None \
                    or timezone.now() - order_express.expressInfoUpdateTime > \
                        timezone.timedelta(hours=1)\
                        or order_express.expressInfoUpdateTime - timezone.now() > \
                        timezone.timedelta(hours=1):
                    _ = get_express_info(order_express)
                    order_express.expressInfo = json.dumps(_) if _ else None
                    order_express.expressInfoUpdateTime = timezone.now()
                    need_update = True
                express_info = json.loads(order_express.expressInfo) if order_express.expressInfo else None
                if express_info and express_info['state'] == '3':   # 签收
                    order_express.expressStatus = 2
                    need_update = True
                if need_update:
                    order_express.save()
            return Response({
                'order_id': order_express.order.id,
                'company': order_express.company.name if order_express.company is not None else '',
                'express_id': order_express.expressId,
                'express_status': order_express.expressStatus,
                'express_status_str': OrderExpress.express_status[order_express.expressStatus][1],
                'traces': None if express_info is None else express_info['traces']
            })
        else:
            return Response({'msg': '请登录'})


class OrderExpressInfoView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        order_info_id = data['order_info_id']
        token = data['token']

        # 参数校验
        if not all([token, order_info_id]):
            return Response({'msg': '数据不完整'})

        # 获取用户open_id
        open_id = PublicFunction().getOpenIdByToken(token)

        data = {}
        # 校验用户
        if open_id:
            try:
                wx_user = WxUser.objects.get(open_id=open_id)
            except:
                return Response({'msg': '用户不存在'})
            try:
                order_info = OrderInfo.objects.get(pk=order_info_id)
            except:
                return Response({'msg': '订单不存在'})
            try:
                order_express = OrderExpress.objects.get(order=order_info)
                if order_express.expressStatus == 0:
                    return Response({'msg': '未发货'})
                if order_express.expressStatus == 2:
                    return Response({'msg': '已收件'})
                express_info = get_express_info(order_express)
                if express_info is None:
                    return Response({'msg': '查询失败'})
                else:
                    return Response(express_info)
            except:
                return Response({'msg': '没有快递信息'})
        else:
            return Response({'msg': '请登录'})

