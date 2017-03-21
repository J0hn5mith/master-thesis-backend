from django.contrib import admin
from alarm.models import AlarmConfig, Alarm


class AlarmConfigAdmin(admin.ModelAdmin):
    pass

admin.site.register(AlarmConfig, AlarmConfigAdmin)


class AlarmAdmin(admin.ModelAdmin):
    pass
admin.site.register(Alarm, AlarmAdmin)
