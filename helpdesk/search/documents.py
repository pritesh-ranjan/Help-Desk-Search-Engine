from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import HelpdeskModel


@registry.register_document
class HelpdeskDocument(Document):
    class Index:
        name = 'helpdesk'

    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }

    class Django:
        model = HelpdeskModel
        fields = [
            'title',
            'details',
            'owner'
        ]
