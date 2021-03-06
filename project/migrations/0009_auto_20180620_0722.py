# Generated by Django 2.0.5 on 2018-06-20 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20180619_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='title')),
                ('description', models.CharField(max_length=200, verbose_name='description')),
                ('status', models.CharField(choices=[('pending', 'pending'), ('started', 'started'), ('closed', 'closed')], max_length=30, verbose_name='status')),
                ('start_date', models.DateTimeField(blank=True, verbose_name='start_date')),
                ('end_date', models.DateTimeField(blank=True, verbose_name='end_date')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.ProjectDetails')),
            ],
        ),
        migrations.RemoveField(
            model_name='projectemployee',
            name='manager',
        ),
    ]
