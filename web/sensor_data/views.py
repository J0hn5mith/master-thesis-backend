import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, Http404
from django.contrib.gis.geos import Point
from rest_framework import viewsets
from rest_framework import status
from tags.models import Tag
from sensor_data.serializers import PositionMeasurementSerializer
from sensor_data.models import PositionMeasurement


class PositionMeasurementViewSet(viewsets.ModelViewSet):
    queryset = PositionMeasurement.objects.all()
    serializer_class = PositionMeasurementSerializer

    def get_queryset(self):
        if 'uid' not in self.request.GET:
            raise Http404

        uid = self.request.GET['uid']

        tag = None
        try:
            tag = Tag.objects.get(uid=uid)
        except Tag.DoesNotExist:
            raise Http404

        user = self.request.user
        if not user.has_perm('view_tag', tag):
            raise Http404

        return PositionMeasurement.objects.all().filter(uid=uid)


@csrf_exempt
def post_position_measurement(request):
    if not request.body:
        raise Http404

    json_str = ((request.body).decode('utf-8'))

    try:
        json_obj = json.loads(json_str)
    except Exception as e:

        return HttpResponse(
            status=status.HTTP_400_BAD_REQUEST,
            content="Json format error: {0}".format(e),
        )

    try:
        sensor_id = json_obj['sensor_id']
        for measurement in json_obj['measurements']:
            position = measurement['position']
            PositionMeasurement.objects.create(
                uid=sensor_id,
                time_stamp=measurement['time_stamp'],
                position=Point(
                    position['longitude'],
                    position['latitude'],
                )
            ).save()
    except KeyError:
        return HttpResponse(
            status=status.HTTP_400_BAD_REQUEST,
            content="JSON is not formated correctly.",
        )

    return JsonResponse({'status': 'ok'})


@csrf_exempt
def post_position_measurement_ttn(request):
    if not request.body:
        raise Http404

    json_str = ((request.body).decode('utf-8'))

    try:
        json_obj = json.loads(json_str)
    except Exception as e:
        return HttpResponse(
            status=status.HTTP_400_BAD_REQUEST,
            content="Json format error: {0}".format(e),
        )

    try:
        sensor_id = json_obj['dev_id']
        position = json_obj['payload_fields']
        time_stamp = json_obj['metadata']['time']

        PositionMeasurement.objects.create(
            uid=sensor_id,
            time_stamp=time_stamp,
            position=Point(
                position['lng'],
                position['lat'],
            )
        ).save()
    except KeyError as e:
        return HttpResponse(
            status=status.HTTP_400_BAD_REQUEST,
            content="JSON has not the required structure: {0}".format(e),
        )

    return JsonResponse({'status': 'ok'})
