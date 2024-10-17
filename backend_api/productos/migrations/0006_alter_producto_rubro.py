# Generated by Django 5.0.6 on 2024-10-12 20:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_producto_imagen'),
        ('rubros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='rubro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rubros', to='rubros.rubro'),
        ),
    ]
