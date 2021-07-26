from django_elasticsearch_dsl import Document, fields, Index

from models import HelpdeskModel

PUBLISHER_INDEX = Index('search_helpdeskmodel')
PUBLISHER_INDEX.segments(number_of_shards=1, number_of_replicas=1)


@PUBLISHER_INDEX.doc_type
class HelpdeskTicket(Document):
    id = fields.IntegerField(attr='id')
    fielddata = True
    title = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
            }
        }
    )
    details = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
            }
        },
    )
    owner = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
            }
        },
    )

    class Django:
        model = HelpdeskModel
