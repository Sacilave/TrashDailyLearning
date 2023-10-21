from django.http import HttpResponse  # 导入http响应的类
from django.shortcuts import render


def mainpage(request):  # 当前需要把用户访问这个url(uniform resource locator)产生响应后自动调用index这个函数(需要把这个url( /products )映射到这个函数)
    return HttpResponse('welcome back')


def index(request):
    return HttpResponse('hello world')

