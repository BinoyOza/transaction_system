from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie import fields


from items.models import Item, ItemVariant


class ItemResource(ModelResource):
    class Meta:
        queryset = Item.objects.all()
        resource_name = 'item'
        authorization = DjangoAuthorization()
        authentication = ApiKeyAuthentication()


class ItemVariantResource(ModelResource):
    item = fields.ForeignKey(ItemResource, 'item')

    class Meta:
        queryset = ItemVariant.objects.all()
        resource_name = 'item_variant'
        authorization = DjangoAuthorization()
        authentication = ApiKeyAuthentication()
