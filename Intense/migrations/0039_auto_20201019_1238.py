# Generated by Django 2.2.15 on 2020-10-19 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intense', '0038_auto_20201019_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='set_time',
            field=models.IntegerField(default=0),
        ),
    ]
