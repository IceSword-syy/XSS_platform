from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cookie(models.Model):
    '''
    Cookie container
    '''
    cookie = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)

    def __unicode__(self):
        return self.cookie
