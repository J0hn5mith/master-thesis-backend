from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserConfiguration


class UserConfigurationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserConfiguration
        fields = (
            'url', 'notify_by_email', 'notify_by_sms', 'has_active_email',
            'has_active_phone',
        )
        read_only = ('url', 'has_active_email', 'has_active_phone', )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    conf = UserConfigurationSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'url', 'username', 'last_name', 'first_name', 'email', 'conf',
        )
        read_only = ('conf', )
