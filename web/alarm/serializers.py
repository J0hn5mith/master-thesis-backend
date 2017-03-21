from rest_framework import serializers
from alarm.models import AlarmConfig, AlarmConfigArea, Alarm


class AlarmConfigAreaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AlarmConfigArea
        fields = ('__all__')


class AlarmConfigSerializer(serializers.HyperlinkedModelSerializer):
    lookup_fieled = 'tag'
    area = AlarmConfigAreaSerializer(read_only=True)

    class Meta:
        model = AlarmConfig
        fields = ('pk', 'tag', 'time_to_deactivate', 'area', 'url')
        read_only_fields = ('pk', 'tag', 'area')

class AlarmSerializer(serializers.HyperlinkedModelSerializer):
    lookup_fieled = 'tag'

    class Meta:
        model = Alarm
        fields = ('state', 'start_time')
        read_only_fields = ('state', 'start_time')
