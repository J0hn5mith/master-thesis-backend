from rest_framework import serializers
from tags.models import Tag
from sensor_data.serializers import PositionMeasurementSerializer


class TagSerializer(serializers.HyperlinkedModelSerializer):
    lookup_fieled = 'pk'
    current_position = PositionMeasurementSerializer()

    class Meta:
        model = Tag
        fields = (
            'pk', 'name', 'charge_status', 'get_status', 'last_update',
            'active', 'avatar', 'uid', 'current_position', 'color',
        )
        read_only_fields = (
            'avatar', 'uid', 'last_update', 'charge_status', 'current_position',
            'color'
        )
