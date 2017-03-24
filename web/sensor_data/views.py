from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from sensor_data.serializers import PositionMeasurementSerializer
from sensor_data.models import PositionMeasurement


class PositionMeasurementViewSet(viewsets.ModelViewSet):
    queryset = PositionMeasurement.objects.all()
    serializer_class = PositionMeasurementSerializer

    def get_queryset(self):
        print("TODO: Check access rights!");
        if 'uid' in self.request.GET:
            return PositionMeasurement.objects.all().filter(uid=self.request.GET['uid'])
        else:
            return PositionMeasurement.objects.all()

# def post_position_measurement(request):
    # json = 'post_position_measurement'

    # sensor_id = 'id'
    # for measurement in measurements:
        # PositionMeasurement.objects.create(
                # uid=sensor_id,
                # time_stamp
                # )


