from django.db import models
from django.contrib.gis.db import models as gis_models


class PositionMeasurement(models.Model):
    uid = models.CharField(
        max_length=16,
    )
    time_stamp = models.DateTimeField()
    position = gis_models.PointField()

    def coordinates(self):
        return {
            "lng": self.position[0],
            "lat": self.position[1],
        }

    class Meta:
        ordering = ['-time_stamp']
