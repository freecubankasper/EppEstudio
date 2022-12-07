# Generated by Django 3.1.2 on 2022-11-02 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyecto', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historialestadoproyecto',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.proyecto'),
        ),
    ]