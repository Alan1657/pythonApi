# Generated by Django 4.2.5 on 2023-10-26 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_pedido_product_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='product',
        ),
        migrations.AddField(
            model_name='pedido',
            name='Customer_pedido',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='customer_pedido', to='api.customer'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='Employee_pedido',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='employee_pedido', to='api.employee'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_stock',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Pedido_detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('pedido_detalle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedido_detalle', to='api.pedido')),
                ('product_pedido', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_pedido', to='api.product')),
            ],
        ),
    ]
