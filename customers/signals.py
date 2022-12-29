from customers.models import Customer
from django.db.models import signals
from tastypie.models import create_api_key

signals.post_save.connect(create_api_key, sender=Customer)
