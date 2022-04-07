from django.db import models

from categories.models import Category
from core.behaviors import ApplicationModelBase


# Create your models here.


class Product(ApplicationModelBase):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    price = models.IntegerField(verbose_name='Precio')
    description = models.TextField(verbose_name='Descripción', null=True)
    image = models.ImageField(upload_to='products', verbose_name="Imagen del Producto")
    category = models.ForeignKey(Category, verbose_name='Categoría', on_delete=models.DO_NOTHING,
                                 related_name='product')

    class Meta:
        db_table = 'products'
        ordering = ['-price']

    def __str__(self):
        return self.name

