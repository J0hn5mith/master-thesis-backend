from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core import urlresolvers
from django.core.files.base import ContentFile
from django.db import models

from avatar_generator import Avatar


class UserConfiguration(models.Model):
    user = models.OneToOneField(
        User,
        related_name='conf',
    )
    avatar = models.ImageField(
        verbose_name=u"Portrait",
        null=True,
        blank=True,
    )

    @classmethod
    def create(cls):
        user_config = cls()
        print("Create")
        return user_config

    def save(self, *args, **kwargs):
        if not self.avatar: self.__generate_avatar()
        super(UserConfiguration, self).save(*args, **kwargs)

    def get_admin_url(self):
        # TODO: Is currently pointing to the real model and not to the conf object
        content_type = ContentType.objects.get_for_model(self.user.__class__)
        return urlresolvers.reverse(
            "admin:%s_%s_change" %
            (content_type.app_label, content_type.model),
            args=(self.user.id, )
        )

    def __generate_avatar(self):
        avatar = Avatar.generate(256, self.user.username)
        self.avatar.save(
            "avatar_" + str(self.pk) + ".png", ContentFile(avatar)
        )
