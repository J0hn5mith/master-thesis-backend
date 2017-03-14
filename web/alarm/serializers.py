from rest_framework import serializers
from alarm.models import AlarmConfig, AlarmConfigArea


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
        # fields = ('__all__')
        read_only_fields = ('pk', 'tag', 'area')
