# Generated by Django 4.1.3 on 2022-11-28 04:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomencladores', '0013_alter_entidad_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='fecha_registro',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 27, 23, 12, 10, 673911)),
        ),
    ]
