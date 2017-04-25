from django.contrib import admin
from tags.models import Tag, SharedTag


class SharedTagInline(admin.TabularInline):
    model = SharedTag


class SharedTagAdmin(admin.ModelAdmin):
    list_display = ('user', 'tag', 'permissions')


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'uid', 'user_with_avatar', 'last_update', 'active', 'color'
    )
    inlines = [
        SharedTagInline,
    ]

admin.site.register(Tag, TagAdmin)
admin.site.register(SharedTag, SharedTagAdmin)
