from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    '''
    Home page
    '''

    return HttpResponse('Hi')
