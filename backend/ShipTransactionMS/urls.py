# jwt内部实现的登陆视图
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.urls import path,include
from django.contrib import admin

# rest_framework
from rest_framework import routers #router路由

router = routers.DefaultRouter() 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('login/', obtain_jwt_token),
    path('login/', obtain_jwt_token),
]