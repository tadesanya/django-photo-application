# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 22:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photomodel',
            options={'ordering': ['-date_created'], 'verbose_name': 'photo', 'verbose_name_plural': 'photos'},
        ),
    ]
