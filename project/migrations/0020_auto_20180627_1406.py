# Generated by Django 2.0.5 on 2018-06-27 14:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_auto_20180627_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasktime',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='start_date'),
        ),
        migrations.AlterField(
            model_name='tasktime',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='start_date'),
        ),
        migrations.AlterField(
            model_name='tasktime',
            name='total_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 27, 14, 6, 54, 807825), verbose_name='start_date'),
        ),
    ]