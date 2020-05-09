# Generated by Django 3.0.5 on 2020-05-08 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_todo_is_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='added_date',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='is_completed',
        ),
        migrations.AddField(
            model_name='todo',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.CharField(max_length=40),
        ),
    ]