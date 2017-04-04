from django.contrib import admin
from alarm.models import AlarmConfig, Alarm, AlarmConfigArea


class AlarmConfigAdmin(admin.ModelAdmin):
    pass


admin.site.register(AlarmConfig, AlarmConfigAdmin)


class AlarmAdmin(admin.ModelAdmin):
    pass


admin.site.register(Alarm, AlarmAdmin)


class AlarmConfigAreaAdmin(admin.ModelAdmin):
    pass


admin.site.register(AlarmConfigArea, AlarmConfigAreaAdmin)
