# Generated by Django 4.1.3 on 2022-11-15 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('llamado', '0005_alter_llamadoproyecto_id'),
        ('evento', '0002_alter_eventoabastecimiento_id_alter_eventoactor_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventoequipamiento',
            name='llamado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='llamado.llamadoproyecto'),
        ),
    ]
