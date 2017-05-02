from rest_framework import serializers
from alarm.models import AlarmConfig, AlarmConfigArea, Alarm
from rest_framework_gis.serializers import GeometrySerializerMethodField


class AlarmConfigAreaSerializer(serializers.HyperlinkedModelSerializer):
    area = GeometrySerializerMethodField()

    def get_area(self, obj):
        return obj.area()

    class Meta:
        model = AlarmConfigArea
        fields = ('url', 'center', 'radius', 'area')
        read_only = ('url', 'area')


class AlarmConfigSerializer(serializers.HyperlinkedModelSerializer):
    lookup_fieled = 'tag'
    area = AlarmConfigAreaSerializer(read_only=True)

    class Meta:
        model = AlarmConfig
        fields = ('pk', 'tag', 'time_to_deactivate', 'area', 'url')
        read_only_fields = ('pk', 'tag', 'area', 'url')


class AlarmSerializer(serializers.HyperlinkedModelSerializer):
    lookup_fieled = 'tag'

    class Meta:
        model = Alarm
        fields = ('state', 'start_time', 'url')
        read_only_fields = ('state', 'start_time', 'url')
