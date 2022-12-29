import json

from django.core.exceptions import ValidationError
from django.db import IntegrityError

from tastypie.authorization import DjangoAuthorization
from tastypie.exceptions import Unauthorized, BadRequest

from customers.models import AssociatedCustomer
from merchants.models import Merchant
from items.models import ItemVariant
from stores.models import Store, StoreItem


class CustomerMerchantAuthorization(DjangoAuthorization):

    def read_list(self, object_list, bundle):
        # Method to return the Model object list.
        return object_list

    def read_detail(self, object_list, bundle):
        # Method to return the Model object data.
        result = super(CustomerMerchantAuthorization, self).read_detail(object_list, bundle)
        return result

    def create_detail(self, object_list, bundle):
        # Get the request body and convert it to JSON.
        request = json.loads(bundle.request.body)
        try:
            # Check whether the user is authenticated or not.
            if not bundle.request.user.is_authenticated:
                raise Unauthorized("You are not allowed to access that resource.")

            # Check whether the Store for merchant being created
            # is associated with the requested user or not.
            if bundle.obj.__class__ == Store:
                self.check_store_permission(bundle, request)
            # Check whether the StoreItem for merchant being created
            # is associated with the requested user or not.
            elif bundle.obj.__class__ == StoreItem:
                self.check_store_item_permission(bundle, request)

            result = super(CustomerMerchantAuthorization, self).create_detail(object_list, bundle)
            # Calling below statement to raise the Duplicate entry error if object exist.
            bundle.obj.save()
            return result
        except (ValidationError, IntegrityError, Exception) as e:
            raise BadRequest(str(e))

    @staticmethod
    def check_store_permission(bundle, request):
        # Associate merchant to the Store model object
        merchant = Merchant.objects.get(id=request.get("merchant"))
        bundle.obj.merchant = merchant

        # Check whether any field/s are missing in the request body.
        if bundle.obj.clean_fields() is None:
            # Check whether the Store for merchant being created
            # is associated with the requested user or not.
            if not AssociatedCustomer.objects.filter(customer=bundle.request.user,
                                                     merchant__id=request.get("merchant")).exists():
                raise Unauthorized("You are not allowed to access that resource.")

    @staticmethod
    def check_store_item_permission(bundle, request):
        # Associate store to the StoreItem model object
        store = Store.objects.get(id=request.get("store"))
        item_variant = ItemVariant.objects.get(id=request.get("item_variant"))
        bundle.obj.store = store
        bundle.obj.item_variant = item_variant

        # Check whether any field/s are missing in the request body.
        if bundle.obj.clean_fields() is None:
            # Check whether the StoreItem for merchant being created
            # is associated with the requested user or not.
            if not AssociatedCustomer.objects.filter(customer=bundle.request.user,
                                                     merchant__id=store.merchant.id).exists():
                raise Unauthorized("You are not allowed to access that resource.")
