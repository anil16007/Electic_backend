# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-22 15:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testingSite', '0002_userinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Userinfo',
        ),
    ]