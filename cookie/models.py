from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ClassName(models.Model):
    '''
    Cookie container
    '''
    cookie = models.CharField(max_length=255)
    # domain = models.CharField(max_length=15)
