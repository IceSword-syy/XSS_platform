# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-01 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookie', models.CharField(max_length=255)),
            ],
        ),
    ]
