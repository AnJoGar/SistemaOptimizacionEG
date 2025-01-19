# Generated by Django 5.0.10 on 2025-01-19 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudCedula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField()),
                ('lugar_nacimiento', models.CharField(max_length=100)),
                ('telefono_contacto', models.CharField(blank=True, max_length=20, null=True)),
                ('email_contacto', models.EmailField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(default='Pendiente', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudPasaporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('fecha_emision', models.DateField()),
                ('telefono_contacto', models.CharField(blank=True, max_length=20, null=True)),
                ('email_contacto', models.EmailField(blank=True, max_length=100, null=True)),
                ('direccion_contacto', models.CharField(blank=True, max_length=200, null=True)),
                ('estado', models.CharField(default='Pendiente', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudVisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('pais_origen', models.CharField(max_length=100)),
                ('motivo_viaje', models.TextField()),
                ('tipo_visa', models.CharField(max_length=100)),
                ('fecha_solicitud', models.DateField()),
                ('numero_pasaporte', models.CharField(max_length=50)),
                ('telefono_contacto', models.CharField(blank=True, max_length=20, null=True)),
                ('email_contacto', models.EmailField(blank=True, max_length=100, null=True)),
                ('estado', models.CharField(default='Pendiente', max_length=20)),
            ],
        ),
    ]
