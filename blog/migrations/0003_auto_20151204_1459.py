# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151204_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='post',
            field=models.ForeignKey(blank=True, to='blog.Post', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='link',
            name='post',
            field=models.ForeignKey(blank=True, to='blog.Post', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, to='blog.Category', null=True),
            preserve_default=True,
        ),
    ]
