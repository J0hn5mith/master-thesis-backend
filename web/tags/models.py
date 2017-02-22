from django.db import models


class Tag(models.Model):

    uid = models.CharField(
        max_length=16,
        unique=True,
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
