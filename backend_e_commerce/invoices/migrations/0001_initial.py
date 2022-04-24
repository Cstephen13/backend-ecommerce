# Generated by Django 4.0.4 on 2022-04-24 00:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('is_active', models.BooleanField(default=True, verbose_name='Estado')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number_invoice', models.IntegerField(default=1)),
                ('total_sale', models.IntegerField(verbose_name='Total venta')),
                ('payment', models.FloatField(verbose_name='Valor Pagado')),
                ('payment_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Pago')),
            ],
            options={
                'db_table': 'invoices',
                'ordering': ['-number_invoice'],
            },
        ),
        migrations.CreateModel(
            name='InvoiceProduct',
            fields=[
                ('is_active', models.BooleanField(default=True, verbose_name='Estado')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(verbose_name='Cantidad')),
                ('price_product', models.IntegerField(verbose_name='Precio')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail_products', to='invoices.invoice', verbose_name='Factura')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Producto')),
            ],
            options={
                'db_table': 'invoice_products',
                'ordering': ['-price_product'],
            },
        ),
        migrations.AddField(
            model_name='invoice',
            name='products',
            field=models.ManyToManyField(through='invoices.InvoiceProduct', to='products.product', verbose_name='Productos'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
