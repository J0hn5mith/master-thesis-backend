from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from tags.models import Tag


class AlarmConfig(models.Model):
    """
    Configures the alarm conditions for a tag.
    """

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
    """
    Signal to automatically create a AlarmConfig for every created tag. Signal
    is used to decouple the instance creation from the tag instance creation.
    """
    if created:
        area = AlarmConfigArea.objects.create()
        AlarmConfig.objects.create(
            tag=instance,
            area=area,
        )


post_save.connect(create_alert_config, Tag)


class AlarmConfigArea(models.Model):
    """
    Defines the area a tag is allowed to be in. Currently
    only supports circular areas.
    """

    center = models.PointField(default=Point(0, 0))
    radius = models.FloatField(
        default=2,
        validators=(MinValueValidator(0), ),
    )


ALARM_STATES = (
    (0, _('Triggered')), (1, _('Pending')), (2, _('Active')),
    (3, _('Canceled')),
)


def generateRandomToken():
    import random
    return ''.join(
        random.choice(settings.RANDOM_TOAKEN_CHARACTERS) for i in range(10)
    )


class Alarm(models.Model):
    """
    Class to represent an alarm state for a tag.
    """
    tag = models.OneToOneField(
        primary_key=True,
        to=Tag,
        related_name='alarm',
        on_delete=models.CASCADE,
    )
    start_position = models.PointField()
    start_time = models.DateTimeField(auto_now_add=True)
    activate_time = models.DateTimeField()
    state = models.IntegerField(
        default=0,
        choices=ALARM_STATES,
    )
    random_token = models.CharField(
        max_length=10, default=generateRandomToken, unique=True
    )
