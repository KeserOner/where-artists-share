# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='art_picture/')),
                ('comment', models.TextField(max_length=500)),
                ('artist', models.ForeignKey(to='artists.Artists')),
            ],
        ),
    ]
