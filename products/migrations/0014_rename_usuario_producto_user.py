# Generated by Django 4.2.6 on 2023-12-13 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_producto_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='usuario',
            new_name='user',
        ),
    ]
