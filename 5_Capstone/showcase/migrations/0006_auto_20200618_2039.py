# Generated by Django 3.0.7 on 2020-06-19 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0005_auto_20200618_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='image',
            field=models.ImageField(null=True, upload_to='media/img'),
        ),
    ]
