from django.contrib import admin
from .models import Cookie

# from django.utils.translation import ugettext

# Register your models here.

class CookieAdmin(admin.ModelAdmin):
    list_display = ('date', 'domain', 'ip', 'update')

admin.site.register(Cookie,CookieAdmin)
