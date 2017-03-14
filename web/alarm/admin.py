from django.contrib import admin
from alarm.models import AlarmConfig

class AlarmConfigAdmin(admin.ModelAdmin):
    pass

admin.site.register(AlarmConfig, AlarmConfigAdmin)
