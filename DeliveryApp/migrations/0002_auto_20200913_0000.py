# Generated by Django 3.1 on 2020-09-12 15:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveryApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='deliveryMethod',
            field=models.CharField(default='개인메뉴', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='createdAt',
            field=models.TimeField(default=datetime.datetime(2020, 9, 13, 0, 0, 35, 723492)),
        ),
    ]