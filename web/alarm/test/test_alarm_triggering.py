from unittest.mock import patch
from django.test import TestCase
from tags.models import Tag
from sensor_data.models import PositionMeasurement
from django.contrib.gis.geos import Point
from django.utils import timezone


class AlarmTriggeringTrestCase(TestCase):
    def setUp(self):
        # Creates alarm config by signal
        self.tag = Tag.objects.create(uid='tag', active=True)

    @patch('alarm.utils.send_alarm_notification')
    def test_new_position_outside_geofence(self, notify):
        PositionMeasurement.objects.create(
            position=Point(10, 10),
            time_stamp=timezone.now(),
            uid='tag',
        )

        self.assertTrue(hasattr(self.tag, 'alarm'))

    @patch('alarm.utils.send_alarm_notification')
    def test_new_position_inside_geofence(self, notify):
        PositionMeasurement.objects.create(
            position=Point(0, 0),
            time_stamp=timezone.now(),
        )
        self.assertFalse(hasattr(self.tag, 'alarm'))
