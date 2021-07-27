from rest_framework import serializers
from search.models import HelpdeskModel


class HelpdeskSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpdeskModel
        fields = ['id', 'title', 'details']
        read_only_fields = ['id', 'title', 'details']
