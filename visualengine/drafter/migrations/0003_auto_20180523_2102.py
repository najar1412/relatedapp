# Generated by Django 2.0.5 on 2018-05-24 01:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('drafter', '0002_auto_20180523_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='basemap',
            name='image',
            field=models.CharField(default=False, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='image',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='herogeometry',
            name='image',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instancemap',
            name='image',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basemap',
            name='init_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 5, 24, 1, 1, 59, 679899, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='herogeometry',
            name='init_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 5, 24, 1, 1, 59, 679899, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='init_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 5, 24, 1, 1, 59, 679899, tzinfo=utc)),
        ),
    ]