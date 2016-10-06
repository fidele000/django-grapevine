# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-06 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0003_email_defaults'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='from_email',
            field=models.CharField(blank=True, db_index=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='email',
            name='subject',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]