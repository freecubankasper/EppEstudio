# Generated by Django 3.1.2 on 2022-11-02 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('llamado', '0002_llamadoproyecto_proyecto'),
    ]

    operations = [
        migrations.AddField(
            model_name='llamadoproyecto',
            name='fecha_fin_llamado',
            field=models.DateTimeField(auto_now=True),
        ),
    ]