from models import HelpdeskModel
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from document import *


class HelpdeskSerializer(DocumentSerializer):
    class Meta:
        model = HelpdeskModel
        document = HelpdeskTicket

        fields = ('title', 'details', 'owner')
