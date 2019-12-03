from django.urls import re_path, path

from .views import *

app_name = 'express'

urlpatterns = [
    path('express/info', OrderExpressView.as_view(), name='info'),
    path('express/traces', OrderExpressInfoView.as_view(), name='traces')
]
