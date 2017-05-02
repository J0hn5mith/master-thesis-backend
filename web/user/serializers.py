from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserConfiguration


class UserConfigurationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserConfiguration
        fields = (
            'url', 'notify_by_email', 'notify_by_sms', 'has_active_email',
            'has_active_phone', 'avatar'
        )
        read_only = ('url', 'has_active_email', 'has_active_phone', 'avatar')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    conf = UserConfigurationSerializer(read_only=True)

    def get_field_names(self, declared_fields, info):
        return super().get_field_names(declared_fields, info)

    class Meta:
        model = User
        fields = (
            'url', 'username', 'last_name', 'first_name', 'email', 'conf', 'pk'
        )
        read_only = ('conf', 'pk')


class LightUserConfigurationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserConfiguration
        fields = ('avatar', )
        read_only = ('__all__', )


class LightUserSerializer(serializers.HyperlinkedModelSerializer):
    """
    User serializer when presenting data to others to maintain a users privacy.
    """
    conf = LightUserConfigurationSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'conf', )
        read_only = ('__all__', )
