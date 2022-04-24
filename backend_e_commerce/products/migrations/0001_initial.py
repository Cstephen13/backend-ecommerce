# Generated by Django 4.0.4 on 2022-04-24 00:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('is_active', models.BooleanField(default=True, verbose_name='Estado')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('price', models.IntegerField(verbose_name='Precio')),
                ('description', models.TextField(null=True, verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='products', verbose_name='Imagen del Producto')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='product', to='categories.category', verbose_name='Categoría')),
            ],
            options={
                'db_table': 'products',
                'ordering': ['-price'],
            },
        ),
    ]
