import datetime
import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from core.behaviors import ApplicationModelBase
from products.models import Product


class Invoice(ApplicationModelBase):
    user = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.DO_NOTHING)
    number_invoice = models.IntegerField(default=1)
    total_sale = models.IntegerField(verbose_name='Total venta')
    payment = models.FloatField(verbose_name='Valor Pagado')
    payment_date = models.DateTimeField(verbose_name='Fecha de Pago', default=datetime.datetime)
    products = models.ManyToManyField(Product, verbose_name='Productos')

    class Meta:
        db_table = 'invoices'
        ordering = ['-number_invoice']

    def __str__(self):
        return f'{self.user} - {self.number_invoice}'

    def save(self, *args, **kwargs):
        if self._state.adding:
            last_id = self.objects.all().aggregate(largest=models.Max('number_invoice'))['largest']
            if last_id is not None:
                self.number_invoice = last_id + 1

        super(Invoice, self).save(*args, **kwargs)
