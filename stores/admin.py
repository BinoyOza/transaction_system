from django.contrib import admin

from stores.models import Store, StoreItem

admin.site.register(Store)
admin.site.register(StoreItem)