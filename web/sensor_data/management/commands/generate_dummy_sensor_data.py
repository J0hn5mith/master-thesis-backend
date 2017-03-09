import sys
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from django.contrib.gis.geos import Point
from sensor_data.models import PositionMeasurement
from tags.models import Tag

User = get_user_model()


class Command(BaseCommand):
    help = 'Generate dummy sensor data'

    def add_arguments(self, parser):
        parser.add_argument(
            '-n',
            dest='num_points',
            default=10,
            type=int,
        )

    def handle(self, *args, **options):
        num_points = int(options['num_points'])

        for p_measurement in PositionMeasurement.objects.all():
            p_measurement.delete()

        for tag_i, tag in enumerate(Tag.objects.all()):
            for i in range(num_points):
                PositionMeasurement.objects.get_or_create(
                    uid=tag.uid,
                    time_stamp=now(),
                    position=Point(47.413220 + i * 0.01, 8.519482 + tag_i * 0.01),
                )
