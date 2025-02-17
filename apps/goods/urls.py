from django.urls import re_path,path

from apps.goods.views import *

app_name = 'goods'

urlpatterns = [
    path('banner/', IndexView.as_view(), name='IndexView'),  # GET
    path('popup/', PopupListView.as_view(), name='PopupListView'),  # GET
    path('sort/', SortListView.as_view(), name='SortListView'),  # GET
    path('goods', GoodsListView.as_view(), name='GoodsListsView'),  # GET
    re_path('goods/id/(?P<goods_id>\d+)', GoodsListViewById.as_view(), name='GoodsListsViewById'),  # GET
    re_path('goods/(?P<sort_id>\d+)/(?P<classify_id>\d+)', GoodsListViewByClassify.as_view(), name='GoodsListViewByClassify'),  # GET
    re_path('goods/(?P<sort_id>\d+)', GoodsListViewBySort.as_view(), name='GoodsListViewScreening'),  # GET
    path('goods/search', GoodsListViewBySearch.as_view(), name='GoodsListViewBySearch'),  # POST 查询关键字产品
    re_path('goods/attribute/(?P<goods_id>\d+)', GoodsAttributeView.as_view(), name='GoodsAttributeView'),  # GET 查询产品属性
    re_path('commodity/get/(?P<commodity_id>\d+)', CommodityListView.as_view(), name='CommodityListView'),  # GET
    re_path('commodity/(?P<goods_id>\d+)', CommodityListViewByGoodsId.as_view(), name='CommodityListViewByGoodsId'), # GET
    path('get/background', UserBackgroundView.as_view(), name='UserBackground'),  # 获取背景图

]
