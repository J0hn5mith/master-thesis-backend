from rest_framework import serializers

from tags.models import Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    lookup_fieled = 'pk'

    class Meta:
        model = Tag
        fields = (
            'pk', 'name', 'charge_status', 'get_status', 'last_update',
            'active', 'avatar',
        )
