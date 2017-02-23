from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import models
from django.utils.html import format_html
from django.utils.translation import ugettext as _


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
        max_digits=3,
        decimal_places=3,
        blank=True,
    )

    def get_status(self):
        return 0

    def user_with_avatar(self):
        return format_html(
            '<a href="{url}"><img src="{0}" width="{size}" height="{size} title="{1}"></img></a>',
            self.user.conf.avatar.url,
            self.user,
            size=25,
            url=self.user.conf.get_admin_url(),
        )
