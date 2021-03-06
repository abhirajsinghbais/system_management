# Generated by Django 2.0.5 on 2018-06-18 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='title')),
                ('description', models.CharField(max_length=200, verbose_name='description')),
                ('status', models.CharField(blank=True, choices=[('pending', 'pending'), ('started', 'started'), ('closed', 'closed')], max_length=30, verbose_name='status')),
                ('start_date', models.DateTimeField(blank=True, verbose_name='start_date')),
                ('end_date', models.DateTimeField(blank=True, verbose_name='end_date')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=30, verbose_name='employee_name')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.ProjectDetails')),],),
    ]
