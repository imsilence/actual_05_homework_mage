# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-15 09:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realname', models.CharField(max_length=64)),
                ('birthday', models.DateField()),
                ('nickname', models.CharField(max_length=64)),
                ('avatar', models.CharField(max_length=256)),
                ('telephone', models.CharField(max_length=32)),
                ('score', models.IntegerField(default=0)),
                ('logintime', models.DateTimeField()),
                ('validkey', models.CharField(max_length=256)),
                ('status', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
