# Generated by Django 4.1.3 on 2022-12-14 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomencladores', '0019_alter_entidad_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='fecha_registro',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 8, 19, 18, 706151)),
        ),
    ]