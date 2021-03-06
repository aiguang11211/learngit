# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-28 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default name', max_length=50)),
                ('user_id', models.IntegerField(default=1)),
                ('user_name', models.CharField(default='default name', max_length=10)),
                ('content', models.CharField(default='default content', max_length=500)),
                ('create_at', models.IntegerField(default=1514879938)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_id', models.IntegerField(default=1)),
                ('user_id', models.IntegerField(default=1)),
                ('user_name', models.CharField(default='default name', max_length=10)),
                ('content', models.CharField(default='default content', max_length=500)),
                ('create_at', models.IntegerField(default=1514879938)),
            ],
        ),
    ]
