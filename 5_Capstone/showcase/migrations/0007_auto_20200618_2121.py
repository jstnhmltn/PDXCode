# Generated by Django 3.0.7 on 2020-06-19 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0006_auto_20200618_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='description',
            field=models.TextField(max_length=100),
        ),
    ]
