# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20151222_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
