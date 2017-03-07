from django.contrib import admin
from sensor_data.models import PositionMeasurement

class PositionMeasurementAdmin(admin.ModelAdmin):
    pass

admin.site.register(PositionMeasurement, PositionMeasurementAdmin)
