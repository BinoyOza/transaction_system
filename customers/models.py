from django.db import models
from django.contrib.auth.models import AbstractUser

from merchants.models import Merchant


# Create your models here.
class Customer(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.username


class AssociatedCustomer(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
