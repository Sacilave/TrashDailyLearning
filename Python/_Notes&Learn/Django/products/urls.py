from django.urls import path  # 用这个可以映射一个url的函数
from . import views  # 其中的 . 指当前文件夹
urlpatterns = [
    path('', views.mainpage),
    path('index', views.index)
]
