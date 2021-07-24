from rest_framework import serializers
from .models import *


class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields = '__all__'


class personnelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Personnel
        fields='__all__'


class shipSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ship
        fields = '__all__'


class inventorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Inventory
        fields = '__all__'


class applicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class certificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'
