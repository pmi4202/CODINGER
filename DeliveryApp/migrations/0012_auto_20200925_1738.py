# Generated by Django 3.1 on 2020-09-25 08:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveryApp', '0011_auto_20200925_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 25, 17, 38, 16, 541473)),
        ),
        migrations.AlterField(
            model_name='order',
            name='deliveryEndTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 25, 17, 38, 16, 541473)),
        ),
        migrations.AlterField(
            model_name='order',
            name='deliveryTime',
            field=models.DateTimeField(default=datetime.timedelta(seconds=1800)),
        ),
    ]
