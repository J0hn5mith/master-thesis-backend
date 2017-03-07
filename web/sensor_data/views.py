from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from sensor_data.serializers import PositionMeasurementSerializer
from sensor_data.models import PositionMeasurement


class PositionMeasurementViewSet(viewsets.ModelViewSet):
    queryset = PositionMeasurement.objects.all()
    serializer_class = PositionMeasurementSerializer

