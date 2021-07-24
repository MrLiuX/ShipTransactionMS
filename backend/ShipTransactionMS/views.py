from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from .models import *
from .serializers import *


class departmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = departmentSerializer


class personnelViewSet(viewsets.ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = personnelSerializer


class shipViewSet(viewsets.ModelViewSet):
    queryset = Ship.objects.all()
    serializer_class = shipSerializer


class inventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = inventorySerializer


class applicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = applicationSerializer


class certificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = certificateSerializer
