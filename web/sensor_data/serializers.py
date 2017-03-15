from rest_framework import serializers
from sensor_data.models import PositionMeasurement


class PositionMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    lookup_fieled = 'pk'

    class Meta:
        model = PositionMeasurement
        fields = ('pk', 'uid', 'time_stamp', 'position', 'coordinates', 'url' )
        read_only_fields = ('pk', 'uid', 'time_stamp', 'position',
                'coordinates', 'url')
