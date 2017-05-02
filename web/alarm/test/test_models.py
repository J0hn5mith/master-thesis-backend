from django.test import TestCase
from tags.models import Tag
from django.contrib.gis.geos import Point
from django.core.exceptions import ValidationError


class AlarmConfigAreaTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create()  # Creates alarm config by signal

    def test_unallowed_change(self):
        self.tag.active = True
        self.tag.save()

        self.tag.alarm_config.area.center = Point(0, 1)
        with self.assertRaises(ValidationError):
            self.tag.alarm_config.area.save()

    def test_allowed_change(self):
        self.tag.active = False
        self.tag.save()

        self.tag.alarm_config.area.center = Point(0, 1)
        try:
            self.tag.alarm_config.area.save()
        except:
            self.assertTrue(False)
