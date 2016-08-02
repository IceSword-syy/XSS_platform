from django.db import models

# Create your models here.

class Cookie(models.Model):

    cookie = models.TextField('Cookie')
    ip = models.CharField('IP',max_length=256)
    domain = models.CharField('From',max_length=256)
    date = models.DateTimeField('Time', auto_now_add=True, editable = True)
    update = models.DateTimeField('Update Time',auto_now=True, null=True)

    def __unicode__(self):
        return self.cookie
