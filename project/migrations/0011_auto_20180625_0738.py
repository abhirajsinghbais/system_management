# Generated by Django 2.0.5 on 2018-06-25 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_task_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetails',
            name='status',
            field=models.CharField(choices=[('Todo', 'Todo'), ('Doing', 'Doing'), ('Done', 'Done')], max_length=30, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='task',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Todo', 'Todo'), ('Doing', 'Doing'), ('Done', 'Done')], max_length=30, verbose_name='status'),
        ),
    ]