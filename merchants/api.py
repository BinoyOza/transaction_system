from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from merchants.models import Merchant


class MerchantResource(ModelResource):
    class Meta:
        queryset = Merchant.objects.all()
        resource_name = 'merchant'
        authorization = Authorization()
