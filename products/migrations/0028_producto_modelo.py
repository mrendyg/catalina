# Generated by Django 4.2.6 on 2024-01-23 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_alter_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='modelo',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='products.modelo'),
            preserve_default=False,
        ),
    ]
