from django.db import models

# Create your models here.

class Cookie(models.Model):
    '''
    class Cookie stores cookies information
    '''

    cookie = models.TextField('Cookie')
    ip = models.CharField('IP',max_length=256)
    domain = models.CharField('From',max_length=256)
    date = models.DateTimeField('Time', auto_now_add=True, editable = True)

    def __unicode__(self):
        return self.cookie
