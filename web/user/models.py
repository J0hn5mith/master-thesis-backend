from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core import urlresolvers
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.signals import post_save
from avatar_generator import Avatar


class UserConfiguration(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='conf',
    )

    avatar = models.ImageField(
        verbose_name=u"Portrait",
        null=True,
        blank=True,
    )

    notify_by_email = models.BooleanField(default=False)

    notify_by_sms = models.BooleanField(default=False)

    @classmethod
    def create(cls):
        user_config = cls()
        return user_config

    def save(self, *args, **kwargs):
        """
        Makes sure all the model's fields are set properly
        """
        if not self.avatar:
            self.__generate_avatar()
        if self.notify_by_email and not self.has_active_email():
            self.notify_by_email = False
        if self.notify_by_sms and not self.has_active_phone():
            self.notify_by_sms = False
        super(UserConfiguration, self).save(*args, **kwargs)

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.user.__class__)
        return urlresolvers.reverse(
            "admin:%s_%s_change" %
            (content_type.app_label, content_type.model),
            args=(self.user.id, ),
        )

    def has_active_email(self):
        """
        Returns whether the user has email address.
        """
        return self.user and self.user.email

    def has_active_phone(self):
        """
        Returns whether there is an active phone registered for the user.
        """
        return self.user and\
            len(self.user.phonedevice_set.filter(confirmed=True)) >= 1

    def __generate_avatar(self):
        avatar = Avatar.generate(256, self.user.username)
        self.avatar.save(
            "avatar_" + str(self.user) + ".png",
            ContentFile(avatar),
            save=False
        )


def create_user_config(sender, instance, created, **kwargs):
    """
    Automatically creates a user conf for every user which is created
    """
    if created:
        try:
            conf, create = UserConfiguration.objects.get_or_create(
                user=instance
            )
        except Exception as e:
            print(e)


post_save.connect(create_user_config, settings.AUTH_USER_MODEL)
