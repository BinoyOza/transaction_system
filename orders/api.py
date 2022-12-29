from tastypie.resources import ModelResource
from tastypie import fields

from orders.models import Order, OrderItem
from stores.api import StoreItemResource


class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'


class OrderItemResource(ModelResource):
    order = fields.ForeignKey(OrderResource, 'order')
    store_item = fields.ForeignKey(StoreItemResource, 'store_item')

    class Meta:
        queryset = OrderItem.objects.all()
        resource_name = 'order_items'
