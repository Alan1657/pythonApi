# Generated by Django 4.2.5 on 2023-10-26 10:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_person_dni_person_person_dni_ruc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='order_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
