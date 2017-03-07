from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from sensor_data.models import PositionMeasurement


class PositionMeasurementSerializer(GeoFeatureModelSerializer):
    lookup_fieled = 'pk'

    class Meta:
        model = PositionMeasurement
        geo_field = 'position'
        fields = ('uid', 'time_stamp', 'position')
        read_only_fields = ('uid', 'time_stamp', 'position')
