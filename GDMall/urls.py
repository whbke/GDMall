"""GDMall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from GDMall import settings
import xadmin

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('docs/', include_docs_urls(title="API文档")),
    path('api/', include('apps.user.urls', namespace='user')),  # 用户模块
    path('api/', include('apps.goods.urls', namespace='goods')),  # 商品模块
    path('api/', include('apps.cart.urls', namespace='cart')),  # 购物车模块
    path('api/', include('apps.card.urls', namespace='card')),  # 购物车模块
    path('api/', include('apps.pay.urls', namespace='pay')),  # 支付模块
    path('api/', include('apps.order.urls', namespace='order')),  # 订单模块
    path('api/', include('apps.express.urls', namespace='express')),  # 快递模块
    path('mdeditor/', include('mdeditor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
