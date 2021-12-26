from django.contrib import admin

from .models import *


class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


admin.site.register(Room, RoomAdmin)