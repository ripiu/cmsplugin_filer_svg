# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-27 13:11
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_svg', '0003_auto_20180327_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='filersvgimagepluginmodel',
            name='link_mailto',
            field=models.EmailField(blank=True, max_length=255, verbose_name='Email address'),
        ),
        migrations.AddField(
            model_name='filersvgimagepluginmodel',
            name='link_phone',
            field=models.CharField(blank=True, max_length=255, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='filersvgimagepluginmodel',
            name='link_page',
            field=cms.models.fields.PageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Page', verbose_name='Internal URL'),
        ),
        migrations.AlterField(
            model_name='filersvgimagepluginmodel',
            name='link_url',
            field=models.URLField(blank=True, max_length=2040, verbose_name='External URL'),
        ),
    ]
