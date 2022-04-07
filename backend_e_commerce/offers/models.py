from django.db import models

# Create your models here.
from core.behaviors import ApplicationModelBase


class Offer(ApplicationModelBase):
    banner = models.ImageField(verbose_name='Banner de Oferta', upload_to='offers')
    init_offer = models.DateTimeField(verbose_name='Fecha de Inicio')
    end_offer = models.DateTimeField(verbose_name='Fecha de Fin')

