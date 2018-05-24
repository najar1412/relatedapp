# Generated by Django 2.0.5 on 2018-05-23 18:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('drafter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemap',
            name='init_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 5, 23, 18, 53, 4, 630264, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='herogeometry',
            name='init_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 5, 23, 18, 53, 4, 630264, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='init_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2018, 5, 23, 18, 53, 4, 630264, tzinfo=utc)),
        ),
    ]