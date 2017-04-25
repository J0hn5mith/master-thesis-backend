import random
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import models
from django.utils.html import format_html
from django.utils.translation import ugettext as _
from colorful.fields import RGBColorField
from sensor_data.models import PositionMeasurement
from sensor_data.serializers import PositionMeasurementSerializer

def get_default_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


class Tag(models.Model):

    uid = models.CharField(
        max_length=16,
        unique=True,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tags',
        blank=True,
        null=True,
    )

    name = models.CharField(
        max_length=128,
        blank=True,
        null=True,
    )

    short_name = models.CharField(
        max_length=16,
        blank=True,
        null=True,
    )

    active = models.BooleanField(default=True)

    last_update = models.DateTimeField(
        null=True,
        blank=True,
    )

    # Null values mean, that the charge status is unknown
    charge_status = models.DecimalField(
        null=True,
        max_digits=6,
        decimal_places=3,
        blank=True,
    )

    avatar = models.ImageField(
        verbose_name=u"Avatar",
        null=True,
        blank=True,
    )

    color = RGBColorField(
            default=get_default_color
            )

    def get_status(self):
        return 0

    def current_position(self):
        sensor_data = PositionMeasurement.objects.filter(
            uid=self.uid
        ).order_by('time_stamp').last()
        return sensor_data

    def user_with_avatar(self):
        if self.user:
            return format_html(
                '<a href="{url}"><img src="{0}" width="{size}" height="{size} title="{1}"></img></a>',
                self.user.conf.avatar.url,
                self.user,
                size=25,
                url=self.user.conf.get_admin_url(),
            )
        else:
            return format_html('None')


# class SharedTag(models.Model):
    # tag = None
    # owner = None

