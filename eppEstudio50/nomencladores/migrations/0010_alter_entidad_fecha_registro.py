# Generated by Django 4.1.3 on 2022-11-15 18:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomencladores', '0009_alter_entidad_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='fecha_registro',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 15, 13, 3, 49, 815113)),
        ),
    ]