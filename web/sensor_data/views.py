import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import Point
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from sensor_data.serializers import PositionMeasurementSerializer
from sensor_data.models import PositionMeasurement


class PositionMeasurementViewSet(viewsets.ModelViewSet):
    queryset = PositionMeasurement.objects.all()
    serializer_class = PositionMeasurementSerializer

    def get_queryset(self):
        print("TODO: Check access rights!")
        if 'uid' in self.request.GET:
            return PositionMeasurement.objects.all().filter(
                uid=self.request.GET['uid']
            )
        else:
            return PositionMeasurement.objects.all()


@csrf_exempt
def post_position_measurement(request):
    if not request.body:
        raise Http404

    data = None
    try:
        data = json.loads(request.body)
    except Exception as e:
        return HttpResponse(
            status=status.HTTP_400_BAD_REQUEST,
            content="Json format error.",
        )
    json_str = ((request.body).decode('utf-8'))
    json_obj = json.loads(json_str)
    sensor_id = json_obj['sensor_id']
    for measurement in json_obj['measurements']:
        try:
            position = measurement['position']
            PositionMeasurement.objects.create(
                uid=sensor_id,
                time_stamp=measurement['time_stamp'],
                position=Point(
                    position['latitude'],
                    position['longitude'],
                )
            ).save()
        except KeyError as e:
            return HttpResponse(
                status=status.HTTP_400_BAD_REQUEST,
                content="JSON is not formated correctly.",
            )

    return JsonResponse({'status': 'ok'})
