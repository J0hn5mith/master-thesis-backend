from rest_framework import viewsets
from alarm.models import AlarmConfig, AlarmConfigArea, Alarm
from alarm.serializers import AlarmConfigSerializer, \
        AlarmConfigAreaSerializer, AlarmSerializer


class AlarmConfigViewSet(viewsets.ModelViewSet):
    queryset = AlarmConfig.objects.all()
    serializer_class = AlarmConfigSerializer


class AlarmConfigAreaViewSet(viewsets.ModelViewSet):
    queryset = AlarmConfigArea.objects.all()
    serializer_class = AlarmConfigAreaSerializer


class AlarmViewSet(viewsets.ModelViewSet):
    queryset = Alarm.objects.all()
    serializer_class = AlarmSerializer
