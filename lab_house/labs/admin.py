from django.contrib import admin

from .models import *


class LabAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'deadline')
    list_display_links = ('id', 'title')


admin.site.register(Lab, LabAdmin)
