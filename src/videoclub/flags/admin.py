from django.contrib import admin

from videoclub.flags.models import Flag


@admin.register(Flag)
class FlagAdmin(admin.ModelAdmin):
    list_filter = ['is_active']
    list_display = ['name', 'is_active', 'updated_at']
    ordering = ['name']
