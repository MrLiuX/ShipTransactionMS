from rest_framework import serializers
from .models import *


class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=[
            'department'
        ]


class personnelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Personnel
        fields=[
            'name',
            'username',
            'password',
            'mobileNumber',
            'teleNumber',
            'address',
            'department'
        ]
