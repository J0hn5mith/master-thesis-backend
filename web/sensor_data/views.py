import json
from django.http import JsonResponse, HttpResponse, Http404
from django.contrib.gis.geos import Point
from tags.models import Tag
from sensor_data.serializers import PositionMeasurementSerializer
from sensor_data.models import PositionMeasurement
import django_filters.rest_framework

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, authentication_classes, \
        permission_classes


class PositionMeasurementViewSet(viewsets.ModelViewSet):
    queryset = PositionMeasurement.objects.all()
    serializer_class = PositionMeasurementSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, )
    filter_fields = ('uid', )

    def get_queryset(self):
        user = self.request.user
        tags = Tag.objects.filter(user=user).values_list('uid', flat=True)
        mes = PositionMeasurement.objects.all()
        mes = mes.filter(uid__in=tags)
        return mes


@authentication_classes((BasicAuthentication, ))
@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
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


@authentication_classes((BasicAuthentication, ))
@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
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
