from rest_framework import serializers
from .models import *


class ExpressCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpressCompany
        fields = '__all__'


class OrderExpressSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderExpress
        fields = '__all__'
