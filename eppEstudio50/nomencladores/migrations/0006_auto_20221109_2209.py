# Generated by Django 3.1.2 on 2022-11-10 03:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomencladores', '0005_auto_20221107_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='fecha_registro',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 22, 9, 47, 105255)),
        ),
    ]
