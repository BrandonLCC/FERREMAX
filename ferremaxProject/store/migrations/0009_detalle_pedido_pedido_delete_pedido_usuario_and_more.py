# Generated by Django 4.2.20 on 2025-05-22 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_pedido_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='detalle_pedido',
            fields=[
                ('id_detalle_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_producto', models.IntegerField()),
                ('precio_producto', models.IntegerField()),
                ('subtotal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('monto_pedido', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('estado', models.CharField(default='Pendiente', max_length=20)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.usuario')),
            ],
        ),
        migrations.DeleteModel(
            name='Pedido_usuario',
        ),
        migrations.AddField(
            model_name='detalle_pedido',
            name='id_pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.pedido'),
        ),
        migrations.AddField(
            model_name='detalle_pedido',
            name='id_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.producto'),
        ),
    ]
