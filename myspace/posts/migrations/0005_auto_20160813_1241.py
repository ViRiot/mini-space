# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-13 17:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_comentario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='fecha_post',
            new_name='fecha',
        ),
    ]
