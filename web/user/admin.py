from django.contrib import admin
from user.models import UserConfiguration

class UserConfigurationAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserConfiguration, UserConfigurationAdmin)
