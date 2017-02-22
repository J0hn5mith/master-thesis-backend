from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django.contrib.staticfiles.templatetags.staticfiles import static


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

    def user_with_avatar(self):
        return format_html(
            '<a href="{url}"><img src="{0}" width="{size}" height="{size} title="{1}"></img></a>',
            self.user.conf.avatar.url,
            self.user,
            size=25,
            url=self.user.conf.get_admin_url(),
        )
