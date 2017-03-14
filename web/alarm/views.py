from rest_framework import viewsets
from alarm.models import AlarmConfig, AlarmConfigArea
from alarm.serializers import AlarmConfigSerializer, AlarmConfigAreaSerializer

class AlarmConfigViewSet(viewsets.ModelViewSet):
    queryset = AlarmConfig.objects.all()
    serializer_class = AlarmConfigSerializer

class AlarmConfigAreaViewSet(viewsets.ModelViewSet):
    queryset = AlarmConfigArea.objects.all()
    serializer_class = AlarmConfigAreaSerializer
