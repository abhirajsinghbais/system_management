# Generated by Django 2.0.5 on 2018-06-20 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_auto_20180619_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date updated'),
        ),
    ]
