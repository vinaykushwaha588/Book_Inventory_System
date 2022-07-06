# Generated by Django 4.0.6 on 2022-07-06 04:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='available_quantity',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(default=datetime.date(2022, 7, 6)),
        ),
        migrations.AlterField(
            model_name='book',
            name='total_quantity',
            field=models.BigIntegerField(),
        ),
    ]
