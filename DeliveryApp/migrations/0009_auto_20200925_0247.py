# Generated by Django 3.1 on 2020-09-24 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveryApp', '0008_auto_20200925_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='createdAt',
            field=models.TimeField(default=datetime.datetime(2020, 9, 25, 2, 47, 18, 573324)),
        ),
        migrations.AlterField(
            model_name='order',
            name='deliveryTime',
            field=models.PositiveIntegerField(default=30),
        ),
    ]