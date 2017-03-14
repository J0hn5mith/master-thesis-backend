from datetime import timedelta
from django.contrib.gis.db import models
from django.contrib.gis.gdal import OGRGeometry
from django.contrib.gis.geos import Point
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from tags.models import Tag


class AlarmConfig(models.Model):
    tag = models.OneToOneField(
        to=Tag,
        primary_key=True,
        related_name='alarm_config',
        on_delete=models.CASCADE,
    )

    area = models.OneToOneField(
        to='AlarmConfigArea',
        on_delete=models.CASCADE,
        null=True,
    )

    time_to_deactivate = models.FloatField(
        default=60.0,
    )




def create_alert_config(sender, instance, created, **kwargs):
    if created:
        area = AlarmConfigArea.objects.create()
        AlarmConfig.objects.create(
            tag=instance,
            area=area,
        )

post_save.connect(create_alert_config, Tag)


class AlarmConfigArea(models.Model):
    """
    Test class only for circular areas.
    """

    center = models.PointField(default=Point(0,0))
    radius = models.FloatField(
        default=2,
        validators=(MinValueValidator(0), ),
    )


# class Alarm(models.Model):
# tag = models.OneToOneField(
# to=Tag,
# on_delete=models.CASCADE,
# )
# start_time = None
# start_position = None
# time_to_deactivate = None
# state = None #Triggered, Pending, Active, Dismissed
