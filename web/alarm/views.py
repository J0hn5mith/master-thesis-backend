from django.http import HttpResponse
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


def cancel(request, random_token):
    """
    Cancels a pending alarm.
    """
    try:
        alarm = Alarm.objects.get(random_token=random_token, state=1)
        alarm.state = Alarm.states.CANCELED
        alarm.save()
        return HttpResponse()
    except Alarm.DoesNotExist:
        return HttpResponse(status=404)


def confirm(request, random_token):
    """
    Confirms a pending alarm.
    """
    try:
        alarm = Alarm.objects.get(random_token=random_token, state=1)
        alarm.state = Alarm.states.ACTIVE
        alarm.save()
        return HttpResponse()
    except Alarm.DoesNotExist:
        return HttpResponse(status=404)
