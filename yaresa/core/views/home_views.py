from django.shortcuts import render

__author__ = 'andrews'


def index(request):
    return render(request,'index.html')

