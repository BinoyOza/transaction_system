from __future__ import unicode_literals

from django.db import models

from items.models import ItemVariant
from merchants.models import Merchant


class Store(models.Model):
    name = models.CharField(max_length=200, unique=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class StoreItem(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    item_variant = models.ForeignKey(ItemVariant, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.store.name} - {self.item_variant.name}"
