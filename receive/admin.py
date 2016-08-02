from django.contrib import admin
from .models import Cookie

# Register your models here.

class CookieAdmin(admin.ModelAdmin):
    list_display = ('date', 'domain', 'ip', 'update')

admin.site.register(Cookie,CookieAdmin)
