# Generated by Django 3.1.2 on 2022-11-02 22:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomencladores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='fecha_registro',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 2, 18, 50, 43, 412245)),
        ),
    ]
