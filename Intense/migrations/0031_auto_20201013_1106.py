# Generated by Django 2.2.15 on 2020-10-13 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Intense', '0030_advertisement_priority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productspecification',
            old_name='quantity',
            new_name='total_quantity',
        ),
    ]