# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'\xe7\xb7\xa8\xe8\x99\x9f', primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255, verbose_name=b'\xe6\xa8\x99\xe9\xa1\x8c')),
                ('type', models.CharField(default=b'normal', max_length=255, verbose_name=b'\xe9\xa1\x9e\xe5\x9e\x8b', choices=[(b'normal', b'\xe4\xb8\x80\xe8\x88\xac'), (b'youtube', b'YouTube'), (b'vimeo', b'Vimeo')])),
                ('body', models.CharField(max_length=255, verbose_name=b'\xe9\x80\xa3\xe7\xb5\x90')),
                ('update_time', models.DateField(auto_now_add=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x99\x82\xe9\x96\x93', db_index=True)),
                ('post', models.ForeignKey(to='blog.Post', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='image',
            name='description',
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(to='blog.Post', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x99\x82\xe9\x96\x93', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(to='blog.Category', null=True),
            preserve_default=True,
        ),
    ]
