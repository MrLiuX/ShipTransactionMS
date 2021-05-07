from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from .models import *
from .serializers import *

class departmentViewSet(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=departmentSerializer


class personnelViewSet(viewsets.ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = personnelSerializer
