# Generated by Django 3.1.2 on 2022-11-02 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nomencladores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=250)),
                ('precio_mlc', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('precio_cup', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('amanecer_img', models.ImageField(blank=True, null=True, upload_to='amanecer_img/')),
                ('mediodia_img', models.ImageField(blank=True, null=True, upload_to='mediodia_img/')),
                ('anochecer_img', models.ImageField(blank=True, null=True, upload_to='anochecer_img/')),
                ('noche_img', models.ImageField(blank=True, null=True, upload_to='noche_img/')),
                ('perfil_lugar_img', models.ImageField(blank=True, null=True, upload_to='perfil_lugar_img/')),
                ('propietario_lugar', models.CharField(max_length=300)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomencladores.municipio')),
                ('sub_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomencladores.subcategoria')),
                ('tipo_arquitectura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomencladores.tipoarquitectura')),
                ('tipo_lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomencladores.tipolugar')),
                ('tipo_suelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nomencladores.tiposuelo')),
            ],
            options={
                'verbose_name': 'locacion',
                'verbose_name_plural': 'locaciones',
                'db_table': 'locacion',
                'ordering': ['id'],
                'permissions': (('enable_locacion', 'Can enable locacion'), ('disable_locacion', 'Can disable locacion'), ('delete_locaciones_seleccionados', 'Can delete locaciones seleccionados'), ('view_menu_locacion', 'Can view menu locacion')),
            },
        ),
    ]