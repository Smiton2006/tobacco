# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-21 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tobacco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tobacco',
            name='img_src',
            field=models.URLField(),
        ),
    ]
