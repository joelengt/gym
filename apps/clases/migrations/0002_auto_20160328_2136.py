# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-29 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestcyclng',
            name='tipo',
            field=models.CharField(choices=[('PRINCIPAL', 'PRINCIPAL'), ('SPINNING', 'SPINNING'), ('BESET CYCLING', 'BEST CYCLING')], max_length=30, unique=True),
        ),
    ]
