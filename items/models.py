from __future__ import unicode_literals

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class ItemVariant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'item')

    def __str__(self):
        return f"{self.item.name} - {self.name}"
