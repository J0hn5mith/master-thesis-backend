from rest_framework import serializers
from tags.models import Tag, SharedTag
from sensor_data.serializers import PositionMeasurementSerializer
from alarm.serializers import AlarmConfigSerializer, AlarmSerializer
from user.serializers import UserSerializer


class TagSerializer(serializers.HyperlinkedModelSerializer):
    lookup_fieled = 'pk'
    current_position = PositionMeasurementSerializer(read_only=True)
    alarm_config = AlarmConfigSerializer(read_only=True)
    alarm = AlarmSerializer(read_only=True)

    class Meta:
        model = Tag
        fields = (
            'pk', 'name', 'charge_status', 'get_status', 'last_update',
            'active', 'avatar', 'uid', 'current_position', 'color',
            'alarm_config', 'alarm', 'url', 'user', 'shared_users'
        )
        read_only_fields = (
            'pk', 'charge_status', 'get_status', 'last_update', 'avatar',
            'current_position', 'color', 'alarm_config', 'url', 'alarm',
            'shared_users'
        )


# class SharedTagSerializer(serializers.HyperlinkedModelSerializer):
class SharedTagSerializer(serializers.ModelSerializer):
    lookup_fieled = 'pk'
    # TODO It might be a good idea to use different serializer
    tag = TagSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = SharedTag
        fields = (
            'pk', 'user', 'tag', 'permissions', 'url',
        )
        read_only = (
            'pk', 'tag', 'url',
        )
