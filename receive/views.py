from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hi, I\'m Le.Wang and I plan to write a small tool to make the exploit of XSS easier.')
