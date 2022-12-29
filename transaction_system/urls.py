"""transaction_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from tastypie.api import Api

from aggregators.api import AggregatorResource
from customers.api import CustomerResource
from items.api import ItemResource, ItemVariantResource
from merchants.api import MerchantResource
from orders.api import OrderResource, OrderItemResource
from stores.api import StoreResource, StoreItemResource

v1_api = Api(api_name="v1")
v1_api.register(AggregatorResource())
v1_api.register(CustomerResource())
v1_api.register(ItemResource())
v1_api.register(ItemVariantResource())
v1_api.register(MerchantResource())
v1_api.register(OrderResource())
v1_api.register(OrderItemResource())
v1_api.register(StoreResource())
v1_api.register(StoreItemResource())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(v1_api.urls)),
]
