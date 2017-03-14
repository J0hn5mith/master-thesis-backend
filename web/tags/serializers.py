from rest_framework import serializers
from tags.models import Tag
from sensor_data.serializers import PositionMeasurementSerializer
from alarm.serializers import AlarmConfigSerializer


class TagSerializer(serializers.HyperlinkedModelSerializer):
    lookup_fieled = 'pk'
    current_position = PositionMeasurementSerializer(read_only=True)
    alarm_config = AlarmConfigSerializer()

    class Meta:
        model = Tag
        fields = (
            'pk', 'name', 'charge_status', 'get_status', 'last_update',
            'active', 'avatar', 'uid', 'current_position', 'color',
            'alarm_config'
        )
        read_only_fields = (
            'pk', 'charge_status', 'get_status', 'last_update', 'avatar',
            'uid', 'current_position', 'color', 'alarm_config'
        )
