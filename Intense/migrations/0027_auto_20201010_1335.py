# Generated by Django 2.2.15 on 2020-10-10 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intense', '0026_auto_20201010_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.IntegerField(blank=True, default=-1),
        ),
    ]
