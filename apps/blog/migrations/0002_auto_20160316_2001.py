# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-17 01:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('created_at',), 'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
        migrations.AlterModelOptions(
            name='imagenes',
            options={'verbose_name': 'Imagen', 'verbose_name_plural': 'Imágenes'},
        ),
        migrations.AlterModelOptions(
            name='ruleta',
            options={'verbose_name': 'Ruleta', 'verbose_name_plural': 'Ruletas'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Video', 'verbose_name_plural': 'Videos'},
        ),
    ]