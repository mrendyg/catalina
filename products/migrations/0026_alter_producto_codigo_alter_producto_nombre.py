# Generated by Django 4.2.6 on 2024-01-23 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_alter_producto_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
