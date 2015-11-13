# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20151103_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='id',
        ),
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.AlterField(
            model_name='author',
            name='AuthorID',
            field=models.CharField(max_length=50, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='AuthorID',
            field=models.ForeignKey(to='book.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(max_length=50, serialize=False, primary_key=True),
        ),
    ]
