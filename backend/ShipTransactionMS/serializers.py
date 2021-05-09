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
