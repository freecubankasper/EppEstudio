# Generated by Django 4.1.3 on 2022-11-28 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0003_eventoequipamiento_llamado'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventoproyecto',
            name='precio_mlc_acumulado',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
