# Generated by Django 2.2.15 on 2020-10-24 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intense', '0002_orderinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(default=-1)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='area_id',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='billing_address_id',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='company_id',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='days',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='delivery_type_id',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='host_site',
            field=models.CharField(blank=True, default='', max_length=264),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='location_id',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='order_id',
            field=models.IntegerField(blank=True, default=-1),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='payment_type',
            field=models.CharField(blank=True, default='', max_length=264),
        ),
    ]