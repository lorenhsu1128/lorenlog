# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'\xe7\xb7\xa8\xe8\x99\x9f', primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'\xe6\xa8\x99\xe9\xa1\x8c', db_index=True)),
                ('slug', models.SlugField(max_length=255, verbose_name=b'\xe7\xb8\xae\xe5\xaf\xab')),
                ('seq', models.IntegerField(default=0, max_length=2, verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
                ('update_time', models.DateField(auto_now_add=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x99\x82\xe9\x96\x93', db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'\xe7\xb7\xa8\xe8\x99\x9f', primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'\xe6\xa8\x99\xe9\xa1\x8c')),
                ('description', models.CharField(max_length=255, verbose_name=b'\xe5\x9c\x96\xe8\xaa\xaa')),
                ('img_file', models.ImageField(upload_to=b'', storage=django.core.files.storage.FileSystemStorage(location=b'/Users/loren/Virtualenvs/loren/loren/blog/static/img'), verbose_name=b'\xe5\x9c\x96\xe6\xaa\x94')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x99\x82\xe9\x96\x93')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'\xe7\xb7\xa8\xe8\x99\x9f', primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255, verbose_name=b'\xe6\xa8\x99\xe9\xa1\x8c')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name=b'\xe7\xb8\xae\xe5\xaf\xab')),
                ('body', models.TextField(verbose_name=b'\xe5\x85\xa7\xe5\xae\xb9')),
                ('update_time', models.DateField(auto_now_add=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x99\x82\xe9\x96\x93', db_index=True)),
                ('category', models.ForeignKey(to='blog.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
