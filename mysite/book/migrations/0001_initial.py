# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AuthorID', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('ISBN', models.CharField(max_length=50)),
                ('AuthorID', models.CharField(max_length=50)),
                ('Publisher', models.CharField(max_length=50)),
                ('PublishDate', models.DateField()),
                ('price', models.CharField(max_length=50)),
            ],
        ),
    ]
