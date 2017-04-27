import random
from django.utils.translation import ugettext as _
from django.conf import settings
from django.db import models
from django.utils.html import format_html
from colorful.fields import RGBColorField
from sensor_data.models import PositionMeasurement


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

    color = RGBColorField(default=get_default_color)

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
                '<a href="{url}"><img src="{0}" width="{size}"\
                    height="{size} title="{1}"></img></a>',
                self.user.conf.avatar.url,
                self.user,
                size=25,
                url=self.user.conf.get_admin_url(),
            )
        else:
            return format_html('None')


class SharedTagPermissions(object):
    ON_ALARM = 0
    READ = 1
    DELEGATE = 2
    ADMIN = 3


SHARED_TAG_PERMISSIONS = (
    (SharedTagPermissions.ON_ALARM, _('On Alarm')),
    (SharedTagPermissions.READ, _('Read Always')),
    (SharedTagPermissions.DELEGATE, _('Read and handle')),
    (SharedTagPermissions.ADMIN, _('Same rights as owner'))
)


class SharedTag(models.Model):
    tag = models.ForeignKey(
        Tag, on_delete=models.CASCADE, related_name="shared_users", null=False
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='shared_tags',
        blank=True,
        null=True,
    )

    permissions = models.IntegerField(
        default=0,
        choices=SHARED_TAG_PERMISSIONS,
    )

    class Meta:
        unique_together = ('tag', 'user')
