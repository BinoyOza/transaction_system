from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.validation import FormValidation

from common.authorization import CustomerMerchantAuthorization

from stores.models import Store, StoreItem
from stores.forms import StoreForm
from items.api import ItemVariantResource


class StoreResource(ModelResource):
    class Meta:
        queryset = Store.objects.all()
        resource_name = "store"
        authorization = CustomerMerchantAuthorization()
        authentication = ApiKeyAuthentication()
        form = FormValidation(form_class=StoreForm)


class StoreItemResource(ModelResource):

    class Meta:
        queryset = StoreItem.objects.all()
        resource_name = "store_items"
        authorization = CustomerMerchantAuthorization()
        authentication = ApiKeyAuthentication()
        form = FormValidation(form_class=StoreItem)
