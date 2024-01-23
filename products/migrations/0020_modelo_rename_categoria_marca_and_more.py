# Generated by Django 4.2.6 on 2024-01-20 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_producto_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('tipo', models.CharField(max_length=50, null=True)),
                ('anio', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Modelo',
            },
        ),
        migrations.RenameModel(
            old_name='Categoria',
            new_name='Marca',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='categoria',
            new_name='marca',
        ),
        migrations.AddField(
            model_name='producto',
            name='modelo',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='products.modelo'),
            preserve_default=False,
        ),
    ]
