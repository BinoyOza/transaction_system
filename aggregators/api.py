from tastypie.resources import ModelResource

from aggregators.models import Aggregator


class AggregatorResource(ModelResource):
    """Resource for Aggregator model."""
    class Meta:
        queryset = Aggregator.objects.all()
        resource_name = 'aggregator'
