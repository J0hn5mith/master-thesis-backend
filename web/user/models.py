from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core import urlresolvers
from django.db import models
from django.db.models.signals import post_save


class UserConfiguration(models.Model):

    user = models.OneToOneField(
        User,
        related_name='conf',
        primary_key=True,
    )

    avatar = models.ImageField(
        verbose_name=u"Portrait",
        null=True,
        blank=True,
    )

    notify_by_email = models.BooleanField(default=True)

    notify_by_sms = models.BooleanField(default=False)

    @classmethod
    def create(cls):
        user_config = cls()
        return user_config

    def save(self, *args, **kwargs):
        if not self.avatar:
            self.__generate_avatar()
        super(UserConfiguration, self).save(*args, **kwargs)

    def get_admin_url(self):
        # TODO: Is currently pointing to
        # the real model and not to the conf object
        content_type = ContentType.objects.get_for_model(self.user.__class__)
        return urlresolvers.reverse(
            "admin:%s_%s_change" %
            (content_type.app_label, content_type.model),
            args=(self.user.id, )
        )

    def __generate_avatar(self):
        pass
        # TODO: fix avatar creation
        # avatar = Avatar.generate(256, self.user.username)

        # from django.core.files.base import ContentFile

        # from avatar_generator import Avatar

        # avatar.save( # "avatar_" + str(self.pk) + ".png", ContentFile(avatar)
        # )


def create_user_config(sender, instance, created, **kwargs):
    """
    Automatically creates a user config for every user which is created
    """
    print("Create user config")
    if created:
        config, created = UserConfiguration.objects.get_or_create(
            user=instance
        )
    pass


# UserD = get_user_model()
post_save.connect(create_user_config, User)
