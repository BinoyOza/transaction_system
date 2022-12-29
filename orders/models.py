from django.db import models

from aggregators.models import Aggregator
from merchants.models import Merchant
from stores.models import StoreItem, Store


# Create your models here.
class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    aggregator = models.ForeignKey(Aggregator, on_delete=models.CASCADE)
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.merchant.name} - {self.store.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    store_item = models.ForeignKey(StoreItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.order} {self.store_item.item.name} ({self.store_item.price})"
