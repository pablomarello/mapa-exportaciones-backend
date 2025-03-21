# Generated by Django 5.0.6 on 2024-08-19 22:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geo', '0001_initial'),
        ('productos', '0004_alter_producto_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exportacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fob_dolar', models.IntegerField(blank=True, null=True)),
                ('peso_neto', models.IntegerField(blank=True, null=True)),
                ('año', models.IntegerField(blank=True, null=True)),
                ('destino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geo.pais')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
        ),
    ]
