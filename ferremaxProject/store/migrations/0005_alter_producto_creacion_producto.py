# Generated by Django 4.2.21 on 2025-05-08 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_producto_creacion_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='creacion_producto',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
