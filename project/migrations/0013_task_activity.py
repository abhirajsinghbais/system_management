# Generated by Django 2.0.5 on 2018-06-25 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_auto_20180625_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='activity',
            field=models.CharField(blank=True, choices=[('Started', 'Started'), ('Play', 'Play'), ('Pause', 'Pause')], max_length=30, verbose_name='activity'),
        ),
    ]
