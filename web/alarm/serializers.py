from rest_framework import serializers
from alarm.models import AlarmConfig, AlarmConfigArea, Alarm


class AlarmConfigAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AlarmConfigArea
        # TODO
        fields = ('url', 'center', 'radius', )
        read_only = ('url')


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
