from django.db import models
from core.behaviors import ApplicationModelBase


# Create your models here.


class Category(ApplicationModelBase):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
