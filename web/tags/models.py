import random
from django.utils.translation import ugettext as _
from django.conf import settings
from django.db import models
from django.utils.html import format_html
from django.db.models.signals import post_save
from colorful.fields import RGBColorField
from sensor_data.models import PositionMeasurement
from guardian.shortcuts import assign_perm


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

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        permissions = (('view_tag', 'View tag'), )

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


def set_tag_permissions(sender, instance, created, **kwargs):
    """
    Set permissions for a newly created tagk
    """
    if instance.user:
        assign_perm('view_tag', instance.user, instance)
        assign_perm('change_tag', instance.user, instance)


post_save.connect(set_tag_permissions, Tag)


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
        permissions = (
            ('view_sharedtag', 'View shared tag'),
        )


def set_shared_tag_permissions(sender, instance, created, **kwargs):
    """
    Set permissions for a newly created tagk
    """
    shared_tag = instance
    if shared_tag.tag and shared_tag.tag.user:
        assign_perm('view_sharedtag', shared_tag.tag.user, instance)
        assign_perm('change_sharedtag', shared_tag.tag.user, instance)

    if shared_tag.user:
        assign_perm('view_sharedtag', shared_tag.user, instance)


post_save.connect(set_shared_tag_permissions, SharedTag)
