from django.db import models
from django.contrib.auth.models import User
from avatar_generator import Avatar
from django.core.files.base import ContentFile

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

    # def avatar_thumbnail(self):
        # return format_html('<img src="{}"></img>', self.avatar.url)

    def __generate_avatar(self):
        avatar = Avatar.generate(256, self.user.username)
        self.avatar.save("avatar_" + str(self.pk) + ".png", ContentFile(avatar))
