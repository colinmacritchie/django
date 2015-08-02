# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationNew',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=120, null=True, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=1000, blank=True)),
                ('description2', models.CharField(max_length=600, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(max_length=50, blank=True)),
                ('zipcode', models.CharField(max_length=5, blank=True)),
                ('state', models.CharField(max_length=10, blank=True)),
                ('city', models.CharField(max_length=50, blank=True)),
                ('country', models.CharField(max_length=50, blank=True)),
            ],
        ),
    ]
