from django.contrib import admin
from tags.models import Tag

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'uid', 'user_with_avatar')
    pass

admin.site.register(Tag, TagAdmin)
