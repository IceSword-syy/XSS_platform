from django.shortcuts import render

from django.http import HttpResponse
from receive.models import Cookie

# Create your views here.

def show_cookie(request):
    '''
    Store cookie information in database
    '''

    s = ''
    for i in Cookie.objects.all():
        s += '<li>' + i.cookie + ' ' + i.domain + ' ' + i.ip + '</li></br>'

    return HttpResponse(s)
